---
title: "How to Add Filters to Your Wall of Love"
url: "https://support.senja.io/how-to-add-filters-to-your-wall-of-love-inudf"
path: "/how-to-add-filters-to-your-wall-of-love-inudf"
---

# How to Add Filters to Your Wall of Love

You can add interactive filter tabs to your Wall of Love so visitors can filter testimonials by category. These tabs appear at the top of your published Wall of Love page, allowing viewers to quickly find testimonials relevant to their interests.

## Overview

Filter tabs create an interactive browsing experience on your Wall of Love. Visitors see clickable tabs (like "All", "Product Features", "Customer Success") at the top of the page. When they click a tab, the testimonials dynamically filter to show only those tagged with the selected category.

> Pro tip: Filter tabs are perfect for showcasing testimonials across different products, industries, or use cases on a single Wall of Love page. Visitors can explore what's most relevant to them without scrolling through everything.

## Prerequisites

Before adding filter tabs:

- You need edit access to the project
- Create tags to categorize your testimonials (e.g., "Enterprise", "Freelancers", "Agencies")
- Assign tags to your testimonials in the Testimonials dashboard
- Have an existing Wall of Love or be ready to create one

> Important: Filter tabs only work with testimonials that have been tagged. Untagged testimonials will only appear under the "All" tab.

## Compatibility

- Available on all Senja plans (Free, Pro, Enterprise)
- Unlimited filter tabs on all plans
- Works on both hosted Wall of Love pages and embedded versions

## How to add filter tabs to your Wall of Love

### Step 1: Navigate to the Wall of Love editor

1. Go to your Studio dashboard.
2. Click the Walls of Love card in the shareables section.
3. Select the Wall of Love you want to edit.

### Step 2: Access the Settings tab

In the Wall of Love editor, click the Settings tab in the sidebar.

Scroll to the Tabs section (also labeled "Section Filters" in some views).

### Step 3: Add your first filter tab

Click the Add filter button (appears as a dashed border with a "+" icon).

A new filter row will appear with options to configure.

### Step 4: Configure your filter tab

For each filter tab, you'll configure:

**Emoji (optional)**

- Click the emoji picker button (round icon).
- Select an emoji to represent this filter.

**Name**

- Enter a descriptive name in the Name field (e.g., "Enterprise Customers", "5-Star Reviews", "SaaS Industry").
- This name will appear as the tab label on your published Wall of Love.

**Pick tags**

- Under the Pick tags section, you'll see a search-based tag picker.
- Type to search for existing tags you've created (e.g., "enterprise", "saas").
- Click tags to select them. You can select multiple tags for a single filter tab.
- Selected tags appear as removable chips with an "x" to delete.
- If you select multiple tags for one filter, testimonials with any of those tags will appear when visitors click that tab.

### Step 5: Add additional filter tabs (optional)

- Click Add filter again to create more tabs.
- Repeat Step 4 to configure each additional filter.
- Drag the grip icon to reorder tabs (the order you set here is how they'll appear on your published page).

As you add filters, the live preview on the right updates in real-time. You'll see tabs appear above your testimonial grid.

### Step 6: Preview your filters

- Check the preview pane on the right side of the editor.
- You should see tabs appearing above your testimonials (e.g., "All", "Features", "Enterprise").
- Changes save automatically after a brief delay (500ms).

### Step 7: Publish and share

1. Click Update or Save changes if prompted to publish your Wall of Love.
2. In the share panel, copy your Wall of Love URL.
3. Share the link or embed your Wall of Love on your website.

## How visitors use filter tabs

When visitors access your published Wall of Love:

1. They see a row of filter tabs at the top of the page (centered or left-aligned based on your design).
2. The first tab is always "All", showing all testimonials.
3. Additional tabs display your custom filters with emojis and names.
4. When a visitor clicks a tab, the testimonial grid animates and filters to show only matching testimonials.
5. The active tab has a darker background to indicate it's selected.

> Best practice: Create 3-6 filter tabs for optimal user experience. Too many tabs can overwhelm visitors, while too few may not provide enough segmentation.

## Verify your setup

To confirm your filter tabs are working correctly:

1. Visit your published Wall of Love URL in a new browser tab.
2. Verify tabs appear at the top of the page.
3. Click each tab and confirm testimonials filter correctly.
4. Check that the "All" tab shows all testimonials.
5. If embedded, test the embed to ensure filters remain functional (note: filters may be hidden if you use `?hideNavigation=true` in the embed URL).

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| No filter tabs appearing on published page | No filters configured in Settings > Tabs | Go to Settings > Tabs in the Wall of Love editor and click "Add filter" to create at least one tab. |
| Empty grid when clicking a filter tab | No testimonials are tagged with the selected filter's tags | Go to your Testimonials dashboard and assign the relevant tags to testimonials. |
| Tags not appearing in tag picker | No tags created yet | Create tags first in your project settings, then return to configure filters. |
| Filter tabs not showing in embedded version | Navigation is hidden in embed URL | Remove `?hideNavigation=true` from your embed URL, or use the full page embed without this parameter. |
| Preview not updating after adding filters | Auto-save delay or browser issue | Wait 1-2 seconds for auto-save, or refresh the preview. Check browser console for errors. |

## Limitations

- Filter tabs only display testimonials that have been tagged -- untagged testimonials only appear under "All"
- Tags must be created before configuring filters (you can't create new tags directly in the filter editor)
- In embedded Walls of Love, tabs may be hidden if `?hideNavigation=true` is in the embed URL
- No mobile swipe gesture for tabs -- visitors click/tap to switch filters
- Filter tab names must be unique within a Wall of Love
- Maximum 120 testimonials can be displayed per Wall of Love (filters apply within this limit)

## What's next

Now that you've added filter tabs to your Wall of Love, you might want to:

- Add tags to multiple testimonials at once to organize them quickly
- Create and manage tags to refine your categorization
- Reorder testimonials within each filter for better presentation
- Customize the background of your Wall of Love to match your brand
- Embed your Wall of Love on your website with filters enabled
