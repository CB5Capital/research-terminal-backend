"""
AI Control Functions for Dashboard Item Management

This module provides OpenAI function definitions for an AI agent that manages
dashboard items by creating, modifying, and deleting items to maintain
an efficient and organized dashboard structure.

The control agent's responsibilities:
1. Eliminate duplicate dashboard items
2. Merge similar items that convey the same information
3. Update outdated information
4. Remove redundant or low-value items
5. Reorganize items for better structure
6. Create summary items when multiple items can be consolidated
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional


def get_control_functions() -> List[Dict[str, Any]]:
    """
    Returns the OpenAI function definitions for dashboard item control operations.
    
    Returns:
        List of function definitions for OpenAI function calling
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "list_dashboard_items",
                "description": "List all current dashboard items for analysis and management",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        }
                    },
                    "required": ["case_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "delete_dashboard_item",
                "description": "Delete a dashboard item that is duplicate, outdated, or redundant",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the dashboard item to delete"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for deletion (e.g., 'duplicate', 'outdated', 'redundant', 'low-value')"
                        }
                    },
                    "required": ["case_name", "item_id", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_dashboard_item",
                "description": "Update an existing dashboard item with new or corrected information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the dashboard item to update"
                        },
                        "updated_component": {
                            "type": "object",
                            "description": "The updated component data (same structure as original component)",
                            "properties": {
                                "type": {"type": "string"},
                                "title": {"type": "string"},
                                "size": {"type": "string"},
                                "sources": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "filename": {"type": "string"},
                                            "relevance": {"type": "string"},
                                            "key_insight": {"type": "string"}
                                        }
                                    }
                                }
                            },
                            "required": ["type"]
                        },
                        "update_reason": {
                            "type": "string",
                            "description": "Reason for the update (e.g., 'merged_duplicates', 'corrected_data', 'enhanced_content')"
                        }
                    },
                    "required": ["case_name", "item_id", "updated_component", "update_reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "create_consolidated_item",
                "description": "Create a new dashboard item that consolidates information from multiple existing items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        },
                        "component": {
                            "type": "object",
                            "description": "The new consolidated component data",
                            "properties": {
                                "type": {"type": "string"},
                                "title": {"type": "string"},
                                "size": {"type": "string"},
                                "sources": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "filename": {"type": "string"},
                                            "relevance": {"type": "string"},
                                            "key_insight": {"type": "string"}
                                        }
                                    }
                                }
                            },
                            "required": ["type", "title"]
                        },
                        "source_item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs that were consolidated into this new item"
                        },
                        "consolidation_reason": {
                            "type": "string",
                            "description": "Reason for consolidation (e.g., 'merged_similar_metrics', 'combined_related_analysis')"
                        }
                    },
                    "required": ["case_name", "component", "source_item_ids", "consolidation_reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "analyze_item_similarity",
                "description": "Analyze similarity between dashboard items to identify duplicates or mergeable content",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        },
                        "item_id_1": {
                            "type": "string",
                            "description": "First item ID to compare"
                        },
                        "item_id_2": {
                            "type": "string",
                            "description": "Second item ID to compare"
                        }
                    },
                    "required": ["case_name", "item_id_1", "item_id_2"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_item_statistics",
                "description": "Get statistics about dashboard items to help with optimization decisions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        }
                    },
                    "required": ["case_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "mark_optimization_complete",
                "description": "Mark the optimization process as complete when no more changes are needed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_name": {
                            "type": "string",
                            "description": "The case name (e.g., 'C1')"
                        },
                        "summary": {
                            "type": "string",
                            "description": "Summary of optimization actions taken"
                        },
                        "final_item_count": {
                            "type": "integer",
                            "description": "Final number of dashboard items after optimization"
                        }
                    },
                    "required": ["case_name", "summary", "final_item_count"]
                }
            }
        }
    ]


def execute_control_function(function_name: str, function_args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a control function call and return the result.
    
    Args:
        function_name: Name of the function to execute
        function_args: Arguments for the function
        
    Returns:
        Dictionary containing the function execution result
    """
    try:
        if function_name == "list_dashboard_items":
            return list_dashboard_items(**function_args)
        elif function_name == "delete_dashboard_item":
            return delete_dashboard_item(**function_args)
        elif function_name == "update_dashboard_item":
            return update_dashboard_item(**function_args)
        elif function_name == "create_consolidated_item":
            return create_consolidated_item(**function_args)
        elif function_name == "analyze_item_similarity":
            return analyze_item_similarity(**function_args)
        elif function_name == "get_item_statistics":
            return get_item_statistics(**function_args)
        elif function_name == "mark_optimization_complete":
            return mark_optimization_complete(**function_args)
        else:
            return {"error": f"Unknown function: {function_name}"}
    except Exception as e:
        return {"error": f"Error executing {function_name}: {str(e)}"}


# Implementation functions

def list_dashboard_items(case_name: str) -> Dict[str, Any]:
    """List all dashboard items for a case."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    if not os.path.exists(items_file):
        return {
            "success": True,
            "items": [],
            "count": 0,
            "message": f"No dashboard items found for case {case_name}"
        }
    
    try:
        with open(items_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
        
        return {
            "success": True,
            "items": items,
            "count": len(items),
            "message": f"Retrieved {len(items)} dashboard items for case {case_name}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to load dashboard items: {str(e)}"
        }


def delete_dashboard_item(case_name: str, item_id: str, reason: str) -> Dict[str, Any]:
    """Delete a dashboard item."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    if not os.path.exists(items_file):
        return {
            "success": False,
            "error": f"No dashboard items file found for case {case_name}"
        }
    
    try:
        # Load current items
        with open(items_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
        
        # Find and remove the item
        original_count = len(items)
        items = [item for item in items if item.get('id') != item_id]
        
        if len(items) == original_count:
            return {
                "success": False,
                "error": f"Item with ID {item_id} not found"
            }
        
        # Save updated items
        with open(items_file, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Deleted item {item_id}. Reason: {reason}",
            "remaining_items": len(items)
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to delete item: {str(e)}"
        }


def update_dashboard_item(case_name: str, item_id: str, updated_component: Dict[str, Any], update_reason: str) -> Dict[str, Any]:
    """Update an existing dashboard item."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    if not os.path.exists(items_file):
        return {
            "success": False,
            "error": f"No dashboard items file found for case {case_name}"
        }
    
    try:
        # Load current items
        with open(items_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
        
        # Find and update the item
        item_found = False
        for item in items:
            if item.get('id') == item_id:
                # Update the component while preserving metadata
                item['component'] = updated_component
                item['metadata']['last_updated'] = datetime.now().isoformat()
                item['metadata']['update_reason'] = update_reason
                item_found = True
                break
        
        if not item_found:
            return {
                "success": False,
                "error": f"Item with ID {item_id} not found"
            }
        
        # Save updated items
        with open(items_file, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Updated item {item_id}. Reason: {update_reason}",
            "updated_component": updated_component
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to update item: {str(e)}"
        }


def create_consolidated_item(case_name: str, component: Dict[str, Any], source_item_ids: List[str], consolidation_reason: str) -> Dict[str, Any]:
    """Create a new consolidated dashboard item."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    # Ensure DashboardLib directory exists
    os.makedirs(os.path.join("DashboardLib", case_name), exist_ok=True)
    
    try:
        # Load current items or create empty list
        items = []
        if os.path.exists(items_file):
            with open(items_file, 'r', encoding='utf-8') as f:
                items = json.load(f)
        
        # Create new consolidated item
        new_item = {
            "id": f"{case_name}_consolidated_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "source_item_ids": source_item_ids,
            "created_at": datetime.now().isoformat(),
            "analysis_type": "consolidated_analysis",
            "component": component,
            "metadata": {
                "component_type": component["type"],
                "consolidation_reason": consolidation_reason,
                "source_items_count": len(source_item_ids),
                "created_by": "control_agent"
            }
        }
        
        # Add the new item
        items.append(new_item)
        
        # Save updated items
        with open(items_file, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Created consolidated item from {len(source_item_ids)} source items",
            "new_item_id": new_item["id"],
            "consolidation_reason": consolidation_reason
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to create consolidated item: {str(e)}"
        }


def analyze_item_similarity(case_name: str, item_id_1: str, item_id_2: str) -> Dict[str, Any]:
    """Analyze similarity between two dashboard items."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    if not os.path.exists(items_file):
        return {
            "success": False,
            "error": f"No dashboard items file found for case {case_name}"
        }
    
    try:
        # Load current items
        with open(items_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
        
        # Find the two items
        item1 = next((item for item in items if item.get('id') == item_id_1), None)
        item2 = next((item for item in items if item.get('id') == item_id_2), None)
        
        if not item1 or not item2:
            return {
                "success": False,
                "error": "One or both items not found"
            }
        
        # Basic similarity analysis
        comp1 = item1.get('component', {})
        comp2 = item2.get('component', {})
        
        similarity_score = 0
        similarity_factors = []
        
        # Type similarity
        if comp1.get('type') == comp2.get('type'):
            similarity_score += 30
            similarity_factors.append("Same component type")
        
        # Title similarity (simple word overlap)
        title1_words = set((comp1.get('title', '') or comp1.get('label', '')).lower().split())
        title2_words = set((comp2.get('title', '') or comp2.get('label', '')).lower().split())
        if title1_words and title2_words:
            word_overlap = len(title1_words.intersection(title2_words)) / len(title1_words.union(title2_words))
            similarity_score += word_overlap * 40
            if word_overlap > 0.3:
                similarity_factors.append(f"Title word overlap: {word_overlap:.2f}")
        
        # Source file similarity
        source1 = item1.get('source_file', '')
        source2 = item2.get('source_file', '')
        if source1 == source2 and source1:
            similarity_score += 20
            similarity_factors.append("Same source file")
        
        # Value similarity for metric cards
        if comp1.get('type') == 'metric_card' and comp2.get('type') == 'metric_card':
            val1 = comp1.get('value', '')
            val2 = comp2.get('value', '')
            if val1 == val2 and val1:
                similarity_score += 10
                similarity_factors.append("Same metric value")
        
        return {
            "success": True,
            "similarity_score": min(similarity_score, 100),
            "similarity_factors": similarity_factors,
            "recommendation": "merge" if similarity_score > 70 else "keep_separate" if similarity_score < 30 else "review",
            "item1_summary": {
                "id": item_id_1,
                "type": comp1.get('type'),
                "title": comp1.get('title') or comp1.get('label', 'Untitled')
            },
            "item2_summary": {
                "id": item_id_2,
                "type": comp2.get('type'),
                "title": comp2.get('title') or comp2.get('label', 'Untitled')
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to analyze similarity: {str(e)}"
        }


def get_item_statistics(case_name: str) -> Dict[str, Any]:
    """Get statistics about dashboard items."""
    items_file = os.path.join("DashboardLib", case_name, "items.json")
    
    if not os.path.exists(items_file):
        return {
            "success": True,
            "statistics": {
                "total_items": 0,
                "by_type": {},
                "by_source_file": {},
                "by_size": {},
                "creation_timeline": []
            }
        }
    
    try:
        # Load current items
        with open(items_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
        
        # Calculate statistics
        stats = {
            "total_items": len(items),
            "by_type": {},
            "by_source_file": {},
            "by_size": {},
            "creation_timeline": []
        }
        
        for item in items:
            component = item.get('component', {})
            
            # Count by type
            item_type = component.get('type', 'unknown')
            stats["by_type"][item_type] = stats["by_type"].get(item_type, 0) + 1
            
            # Count by source file
            source_file = item.get('source_file', 'unknown')
            stats["by_source_file"][source_file] = stats["by_source_file"].get(source_file, 0) + 1
            
            # Count by size
            size = component.get('size', 'unknown')
            stats["by_size"][size] = stats["by_size"].get(size, 0) + 1
            
            # Creation timeline
            created_at = item.get('created_at', '')
            if created_at:
                stats["creation_timeline"].append({
                    "id": item.get('id'),
                    "created_at": created_at,
                    "type": item_type
                })
        
        # Sort timeline by creation date
        stats["creation_timeline"].sort(key=lambda x: x.get('created_at', ''))
        
        return {
            "success": True,
            "statistics": stats
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get statistics: {str(e)}"
        }


def mark_optimization_complete(case_name: str, summary: str, final_item_count: int) -> Dict[str, Any]:
    """Mark the optimization process as complete."""
    try:
        # Create optimization log
        optimization_log = {
            "case_name": case_name,
            "completed_at": datetime.now().isoformat(),
            "summary": summary,
            "final_item_count": final_item_count,
            "optimization_completed": True
        }
        
        # Save optimization log
        log_dir = os.path.join("DashboardLib", case_name)
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(log_dir, "optimization_log.json")
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(optimization_log, f, indent=2, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Optimization completed for case {case_name}",
            "summary": summary,
            "final_item_count": final_item_count,
            "optimization_completed": True
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to mark optimization complete: {str(e)}"
        }