# Background Speech Denoising Documentation

## Overview

Vapi provides two complementary noise filtering technologies. As the documentation states, "Smart Denoising alone provides excellent results" for most situations, while Fourier denoising is experimental and requires significant tuning.

## Two Denoising Methods

**Smart Denoising (Krisp):** Uses AI to remove real-time background noise from common sources like typing, conversations, traffic, and appliances.

**Fourier Denoising:** A frequency-domain filtering approach with customizable parameters. The guide emphasizes this is "highly experimental" and should only supplement Smart Denoising when necessary.

## Configuration

Both methods configure through the `backgroundSpeechDenoisingPlan` property on your assistant, available in TypeScript, Python, and cURL implementations.

Smart Denoising requires only a boolean `enabled` flag. Fourier denoising offers four tunable parameters:
- `baselineOffsetDb`: Controls filtering aggression (-30 to -5)
- `windowSizeMs`: Sets adaptation speed (1000 to 30000)
- `baselinePercentile`: Focuses detection on speech levels (1 to 99)
- `staticThreshold`: Fallback threshold in dB (-80 to 0)

## Key Recommendations

Start with Smart Denoising only. Add Fourier denoising only when "specific requirements that Smart Denoising cannot address" exist. The documentation warns against using Fourier alone, as it's designed to complement rather than replace Smart Denoising.

Environment-specific presets are provided for quiet offices, noisy call centers, and homes with media backgrounds.
