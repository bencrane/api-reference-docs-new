# Legacy Voice Migration Guide

## Overview

Vapi retired legacy voices on March 1, 2026, and introduced new ultra-realistic voice clones. The documentation explains what changed and how users can update their assistants.

## Key Changes

**Retired Voices (8 total):**
Spencer, Neha, Harry, Cole, Paige, Hana, Lily, and Kylie are no longer available.

**Retained Voices (11 total):**
Elliot, Savannah, Rohan, Leo, Zoe, Mia, Jess, Zac, Dan, Leah, and Tara continue with full support.

**New Voices (7 available):**
Emma, Nico, Neil, Sagar, Kai, Clara, and Godfrey represent the next generation of voice options.

## Migration Details

Assistants using discontinued voices were automatically reassigned to replacement options selected via ElevenLabs' voice matching technology. The default replacement (Option 1) prioritized tonal and stylistic similarity while maintaining comparable pricing.

Users can manually switch voices anytime through the dashboard or API by updating the `voiceId` field in their assistant configuration.

## Support

The documentation notes that "Your account team will reach out with personalized support" for Enterprise customers, with general support available at support@vapi.ai.
