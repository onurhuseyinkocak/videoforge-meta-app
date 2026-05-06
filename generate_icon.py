#!/usr/bin/env python3
"""Generate VideoForge app icon (1024x1024 PNG)."""

from PIL import Image, ImageDraw
import math

def generate_videoforge_icon():
    """Create a modern app icon with play button and gradient accent."""

    # Canvas setup
    size = 1024
    img = Image.new('RGB', (size, size), color='#1a1a2e')
    draw = ImageDraw.Draw(img, 'RGBA')

    center_x, center_y = size // 2, size // 2

    # Subtle vignette effect (darkening toward edges)
    for i in range(0, size // 2, 5):
        alpha = int(15 * (i / (size // 2)))
        draw.ellipse(
            [(center_x - i, center_y - i),
             (center_x + i, center_y + i)],
            outline=(0, 0, 0, alpha),
            width=5
        )

    # Create play button icon (stylized V-shape + play triangle)
    icon_size = 380
    icon_left = center_x - icon_size // 2
    icon_top = center_y - icon_size // 2

    # Define play button triangle points (right-pointing)
    # Large isosceles triangle
    play_left = icon_left + 80
    play_top = icon_top + 50
    play_right = icon_left + icon_size - 80
    play_bottom = icon_top + icon_size - 50

    # Triangle vertices: left point, top-right, bottom-right
    play_points = [
        (play_left, (play_top + play_bottom) // 2),  # Left apex
        (play_right, play_top),                        # Top-right
        (play_right, play_bottom)                      # Bottom-right
    ]

    # Draw play button with gradient effect using electric blue -> orange
    # Primary fill: electric blue
    draw.polygon(play_points, fill='#00d4ff')

    # Add orange accent stripe (right edge)
    accent_width = 40
    draw.polygon([
        (play_right - accent_width, play_top),
        (play_right, play_top),
        (play_right, play_bottom),
        (play_right - accent_width, play_bottom)
    ], fill='#ff6b35')

    # Add highlight shine (top-left of play button)
    shine_size = icon_size // 3
    shine_points = [
        (play_left, (play_top + play_bottom) // 2),
        (play_left + shine_size, play_top + shine_size),
        (play_left + shine_size * 0.6, play_top + shine_size * 0.6)
    ]
    draw.polygon(shine_points, fill=(255, 255, 255, 60))

    # Add outer ring accent (geometric circle)
    ring_radius = icon_size // 2 + 30
    ring_width = 12

    # Draw electric blue ring
    ring_bbox = [
        center_x - ring_radius,
        center_y - ring_radius,
        center_x + ring_radius,
        center_y + ring_radius
    ]
    draw.ellipse(ring_bbox, outline='#00d4ff', width=ring_width)

    # Add orange accent on ring (quarter circle at top)
    ring_start_angle = -90
    ring_end_angle = 0

    # Draw orange accent arc via polygon approximation
    num_points = 30
    arc_points = []
    for i in range(num_points + 1):
        angle = ring_start_angle + (ring_end_angle - ring_start_angle) * (i / num_points)
        rad = math.radians(angle)

        # Outer point
        x_outer = center_x + ring_radius * math.cos(rad)
        y_outer = center_y + ring_radius * math.sin(rad)
        arc_points.append((x_outer, y_outer))

    # Inner arc
    inner_radius = ring_radius - ring_width
    for i in range(num_points, -1, -1):
        angle = ring_start_angle + (ring_end_angle - ring_start_angle) * (i / num_points)
        rad = math.radians(angle)
        x_inner = center_x + inner_radius * math.cos(rad)
        y_inner = center_y + inner_radius * math.sin(rad)
        arc_points.append((x_inner, y_inner))

    if len(arc_points) > 2:
        draw.polygon(arc_points, fill='#ff6b35')

    # Save the icon
    output_path = '/Users/jinx/Documents/projeler/videoforge-meta-app/app-icon.png'
    img.save(output_path, 'PNG')
    print(f"✓ Icon generated: {output_path}")
    print(f"  Size: {size}x{size}")
    print(f"  Colors: Dark navy (#1a1a2e), Electric blue (#00d4ff), Orange (#ff6b35)")

if __name__ == '__main__':
    generate_videoforge_icon()
