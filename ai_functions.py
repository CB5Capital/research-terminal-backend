"""
AI Functions for OpenAI Agents to Create Dashboard Items

This module defines functions that OpenAI agents can use to create various types
of dashboard items. Each function corresponds to a specific dashboard component type
that can be rendered in the frontend.
"""

from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime


def create_metric_card(
    label: str,
    value: str,
    size: str = "small",
    color: str = "blue",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a metric card dashboard component.
    
    Args:
        label: The label/title for the metric (e.g., "Market Size by 2029")
        value: The metric value (e.g., "$45.2B", "23.5%")
        size: Component size - "small", "medium", or "large"
        color: Color theme - "blue", "green", "red", "orange", "purple"
        source_filename: Source file for this data
        key_insight: Brief description of what this metric represents
        
    Returns:
        Dictionary representing a metric card component
    """
    component = {
        "type": "metric_card",
        "size": size,
        "label": label,
        "value": value,
        "color": color
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Metric: {label}"
        }]
    
    return component


def create_data_table(
    title: str,
    headers: List[str],
    rows: List[List[str]],
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a data table dashboard component.
    
    Args:
        title: Table title
        headers: List of column headers
        rows: List of rows, where each row is a list of cell values
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this table shows
        
    Returns:
        Dictionary representing a data table component
    """
    component = {
        "type": "data_table",
        "size": size,
        "title": title,
        "headers": headers,
        "rows": rows
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Table data: {title}"
        }]
    
    return component


def create_financial_chart(
    title: str,
    data: List[Dict[str, Any]],
    chart_type: str = "bar",
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a financial chart dashboard component.
    
    Args:
        title: Chart title
        data: List of data points, each with "label" and "value" keys
        chart_type: Type of chart - "bar", "line", "pie", "area"
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this chart shows
        
    Returns:
        Dictionary representing a financial chart component
    """
    component = {
        "type": "financial_chart",
        "size": size,
        "title": title,
        "data": data,
        "chart_type": chart_type
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Chart data: {title}"
        }]
    
    return component


def create_list_items(
    title: str,
    items: List[str],
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a list items dashboard component.
    
    Args:
        title: List title
        items: List of string items to display
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this list represents
        
    Returns:
        Dictionary representing a list items component
    """
    component = {
        "type": "list_items",
        "size": size,
        "title": title,
        "items": items
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"List: {title}"
        }]
    
    return component


def create_short_text(
    title: str,
    content: str,
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a short text dashboard component.
    
    Args:
        title: Text title
        content: Text content (should be brief, 1-2 sentences)
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this text represents
        
    Returns:
        Dictionary representing a short text component
    """
    component = {
        "type": "short_text",
        "size": size,
        "title": title,
        "content": content
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "Medium",
            "key_insight": key_insight or f"Short text: {title}"
        }]
    
    return component


def create_long_text(
    title: str,
    content: str,
    size: str = "large",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a long text dashboard component.
    
    Args:
        title: Text title
        content: Text content (can be longer, multiple paragraphs)
        size: Component size - "medium" or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this text represents
        
    Returns:
        Dictionary representing a long text component
    """
    component = {
        "type": "long_text",
        "size": size,
        "title": title,
        "content": content
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Long text analysis: {title}"
        }]
    
    return component


def create_text_analysis(
    title: str,
    content: str,
    insights: Optional[List[str]] = None,
    conclusion: Optional[str] = None,
    size: str = "large",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a text analysis dashboard component.
    
    Args:
        title: Analysis title
        content: Main analysis content
        insights: Optional list of key insights
        conclusion: Optional conclusion summary
        size: Component size - "medium" or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this analysis covers
        
    Returns:
        Dictionary representing a text analysis component
    """
    component = {
        "type": "text_analysis",
        "size": size,
        "title": title,
        "content": content,
        "insights": insights,
        "conclusion": conclusion
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Analysis: {title}"
        }]
    
    return component


def create_competitor_analysis(
    title: str,
    competitors: List[Dict[str, str]],
    size: str = "large",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a competitor analysis dashboard component.
    
    Args:
        title: Analysis title
        competitors: List of competitor dicts with keys: "name", "market_share", "key_strength", "position"
        size: Component size - "medium" or "large"
        source_filename: Source file for this data
        key_insight: Brief description of the competitive analysis
        
    Returns:
        Dictionary representing a competitor analysis component
    """
    component = {
        "type": "competitor_analysis",
        "size": size,
        "title": title,
        "competitors": competitors
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Competitor analysis: {title}"
        }]
    
    return component


def create_risk_assessment(
    title: str,
    risks: List[Dict[str, str]],
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a risk assessment dashboard component.
    
    Args:
        title: Assessment title
        risks: List of risk dicts with keys: "title", "level", "description"
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of the risk assessment
        
    Returns:
        Dictionary representing a risk assessment component
    """
    component = {
        "type": "risk_assessment",
        "size": size,
        "title": title,
        "risks": risks
    }
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "High",
            "key_insight": key_insight or f"Risk assessment: {title}"
        }]
    
    return component


def create_progress_bar(
    title: str,
    value: float,
    max_value: float = 100.0,
    label: str = None,
    color: str = "blue",
    size: str = "medium",
    source_filename: str = None,
    key_insight: str = None
) -> Dict[str, Any]:
    """
    Create a progress bar dashboard component.
    
    Args:
        title: Progress bar title
        value: Current value
        max_value: Maximum value (default 100.0)
        label: Optional label to display with the progress
        color: Color theme - "blue", "green", "red", "orange", "purple"
        size: Component size - "small", "medium", or "large"
        source_filename: Source file for this data
        key_insight: Brief description of what this progress represents
        
    Returns:
        Dictionary representing a progress bar component
    """
    component = {
        "type": "progress_bar",
        "size": size,
        "title": title,
        "value": value,
        "max_value": max_value,
        "color": color
    }
    
    if label:
        component["label"] = label
    
    if source_filename:
        component["sources"] = [{
            "filename": source_filename,
            "relevance": "Medium",
            "key_insight": key_insight or f"Progress metric: {title}"
        }]
    
    return component


# OpenAI Function Definitions for Function Calling
OPENAI_FUNCTIONS = [
    {
        "type": "function",
        "function": {
            "name": "create_metric_card",
            "description": "Create a metric card to display a key performance indicator or important metric",
            "parameters": {
                "type": "object",
                "properties": {
                    "label": {
                        "type": "string",
                        "description": "The label/title for the metric (e.g., 'Market Size by 2029', 'Growth Rate')"
                    },
                    "value": {
                        "type": "string",
                        "description": "The metric value (e.g., '$45.2B', '23.5%', '1,250 units')"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "color": {
                        "type": "string",
                        "enum": ["blue", "green", "red", "orange", "purple"],
                        "description": "Color theme for the metric card"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this metric represents"
                    }
                },
                "required": ["label", "value"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_data_table",
            "description": "Create a data table to display structured data in rows and columns",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Table title"
                    },
                    "headers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of column headers"
                    },
                    "rows": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "description": "List of rows, where each row is a list of cell values"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this table shows"
                    }
                },
                "required": ["title", "headers", "rows"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_financial_chart",
            "description": "Create a financial chart to visualize numerical data",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Chart title"
                    },
                    "data": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "label": {"type": "string"},
                                "value": {"type": "number"}
                            },
                            "required": ["label", "value"]
                        },
                        "description": "List of data points with label and value"
                    },
                    "chart_type": {
                        "type": "string",
                        "enum": ["bar", "line", "pie", "area"],
                        "description": "Type of chart to display"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this chart shows"
                    }
                },
                "required": ["title", "data"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_list_items",
            "description": "Create a bulleted list to display multiple related items",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "List title"
                    },
                    "items": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of string items to display"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this list represents"
                    }
                },
                "required": ["title", "items"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_short_text",
            "description": "Create a short text component for brief summaries or key points",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Text title"
                    },
                    "content": {
                        "type": "string",
                        "description": "Text content (should be brief, 1-2 sentences)"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this text represents"
                    }
                },
                "required": ["title", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_long_text",
            "description": "Create a long text component for detailed analysis or explanations",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Text title"
                    },
                    "content": {
                        "type": "string",
                        "description": "Text content (can be longer, multiple paragraphs)"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this text represents"
                    }
                },
                "required": ["title", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_text_analysis",
            "description": "Create a comprehensive text analysis component with insights and conclusions",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Analysis title"
                    },
                    "content": {
                        "type": "string",
                        "description": "Main analysis content"
                    },
                    "insights": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of key insights"
                    },
                    "conclusion": {
                        "type": "string",
                        "description": "Optional conclusion summary"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this analysis covers"
                    }
                },
                "required": ["title", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_competitor_analysis",
            "description": "Create a competitor analysis component to compare market competitors",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Analysis title"
                    },
                    "competitors": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "market_share": {"type": "string"},
                                "key_strength": {"type": "string"},
                                "position": {"type": "string"}
                            },
                            "required": ["name", "market_share", "key_strength", "position"]
                        },
                        "description": "List of competitors with their details"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of the competitive analysis"
                    }
                },
                "required": ["title", "competitors"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_risk_assessment",
            "description": "Create a risk assessment component to analyze potential risks",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Assessment title"
                    },
                    "risks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "level": {"type": "string"},
                                "description": {"type": "string"}
                            },
                            "required": ["title", "level", "description"]
                        },
                        "description": "List of risks with their details"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of the risk assessment"
                    }
                },
                "required": ["title", "risks"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_progress_bar",
            "description": "Create a progress bar to show completion or achievement levels",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Progress bar title"
                    },
                    "value": {
                        "type": "number",
                        "description": "Current value"
                    },
                    "max_value": {
                        "type": "number",
                        "description": "Maximum value (default 100.0)"
                    },
                    "label": {
                        "type": "string",
                        "description": "Optional label to display with the progress"
                    },
                    "color": {
                        "type": "string",
                        "enum": ["blue", "green", "red", "orange", "purple"],
                        "description": "Color theme for the progress bar"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["small", "medium", "large"],
                        "description": "Component size"
                    },
                    "source_filename": {
                        "type": "string",
                        "description": "Source filename where this data came from"
                    },
                    "key_insight": {
                        "type": "string",
                        "description": "Brief description of what this progress represents"
                    }
                },
                "required": ["title", "value"]
            }
        }
    }
]


# Helper function to get all functions as a list for OpenAI
def get_openai_functions():
    """Return the list of OpenAI function definitions."""
    return OPENAI_FUNCTIONS


# Function mapping for dynamic execution
FUNCTION_MAPPING = {
    "create_metric_card": create_metric_card,
    "create_data_table": create_data_table,
    "create_financial_chart": create_financial_chart,
    "create_list_items": create_list_items,
    "create_short_text": create_short_text,
    "create_long_text": create_long_text,
    "create_text_analysis": create_text_analysis,
    "create_competitor_analysis": create_competitor_analysis,
    "create_risk_assessment": create_risk_assessment,
    "create_progress_bar": create_progress_bar,
}


def execute_function_call(function_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a function call from OpenAI function calling.
    
    Args:
        function_name: Name of the function to execute
        arguments: Dictionary of function arguments
        
    Returns:
        Dictionary representing the dashboard component
        
    Raises:
        ValueError: If function_name is not recognized
    """
    if function_name not in FUNCTION_MAPPING:
        raise ValueError(f"Unknown function: {function_name}")
    
    function = FUNCTION_MAPPING[function_name]
    return function(**arguments)