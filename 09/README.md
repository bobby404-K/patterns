# Pattern 09: Diamond Star Pattern

## Intuition
A full diamond shape using stars. It is created by combining an erect Star Pyramid (Pattern 07) and an Inverted Star Pyramid (Pattern 08) vertically.

## Approach
1. **Upper Pyramid:**
   - Run loop `i` from `0` to `N-1`.
   - Print `N - i - 1` spaces, `2 * i + 1` stars, and `N - i - 1` spaces.
2. **Lower Inverted Pyramid:**
   - Run loop `i` from `0` to `N-1`.
   - Print `i` spaces, `2 * N - (2 * i + 1)` stars, and `i` spaces.

## Complexity
- **Time Complexity:** `O(N²)` — Both upper and lower pyramids take `O(N²)` time.
- **Space Complexity:** `O(1)` — Constant extra space.
