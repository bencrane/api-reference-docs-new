# Boards Quickstart Documentation

## Overview
Vapi's Boards feature enables teams to create custom analytics dashboards with real-time insights through a drag-and-drop interface within the Vapi Dashboard.

## Key Capabilities
The platform supports:
- Multiple widget types (bar charts, line charts, pie charts, text metrics)
- Visual query building with field selectors and filters
- Custom calculated metrics using Math.js formulas
- Responsive grid layout with drag-and-resize functionality
- Global time range filters and granularity settings

## Ideal Use Cases
- **Sales tracking**: Monitor call volume, conversion rates, booking metrics
- **Support metrics**: Track resolution times, issue categories, satisfaction scores
- **Cost monitoring**: Analyze spending patterns and budget tracking
- **Performance analysis**: Measure assistant performance and call quality

## Getting Started Process

### Access & Initial Setup
Users log into dashboard.vapi.ai, navigate to Boards in the sidebar, and receive an automatically-generated 6-column grid layout on first visit.

### Building a Dashboard
The quickstart guides creation of a Sales Performance Dashboard containing:
1. Text metrics for total calls and bookings
2. Bar charts for calls-by-assistant
3. Line charts for volume trends
4. Pie charts for outcome distribution
5. Calculated metrics for conversion rates

### Key Features Explained

**Text Insights**: Display single important metrics with real-time updates

**Chart Types**:
- Line charts excel at "showing trends over time"
- Bar charts compare categories
- Pie charts display proportional breakdowns (not time-series)

**Filtering**: Multiple conditions can be stacked using field selectors, operators (equals, greater-than), and specific values

**Calculated Metrics**: Custom formulas support syntax like:
```
({{totalBookings}} / {{totalCalls}}) * 100
```

## Organization & Optimization

**Layout best practices**:
- Position critical metrics prominently
- Group related insights together
- Maintain consistent sizing for similar widgets
- KPI cards: 1-2 columns; Charts: 3-4 columns

**Performance considerations**: Boards with 10+ complex insights may load slower; use appropriate time ranges to optimize performance.

## Advanced Functionality

**Global filters**: Time range picker and granularity selector update all insights simultaneously

**Fullscreen mode**: Display dashboards on TV screens or for presentations

**Formula editor**: Supports variable autocomplete and validation, accepting all Math.js operations

## Troubleshooting
Common issues include: "No data" results (narrow time ranges), unresponsive drag functionality (requires drag-handle icon), and formula errors (variables must be wrapped in `{{}}` syntax).

## Prerequisites
Users need a Vapi account with Boards access enabled and existing call data for meaningful visualizations.
