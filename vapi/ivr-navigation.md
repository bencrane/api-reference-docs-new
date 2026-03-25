# IVR Navigation Guide Summary

## Key Overview
Vapi provides the DTMF tool enabling assistants to navigate IVR menus by entering digits such as member IDs and account numbers. The guide addresses timing and formatting challenges to improve reliability.

## Main Recommendations

**Pause Between Digits**
"Some IVRs buffer audio or expect digits at a slower pace" causing missed inputs. Different providers use distinct pause syntax—Twilio uses `w` (0.5s) and `W` (1s), while Vonage employs `p` for 0.5s pauses.

**Allow Menu Completion**
Assistants should wait for all options before responding. The guide recommends "Reply with an empty string like ' ' to ensure nothing is spoken" while awaiting IVR completion.

**Progressive Retry Strategy**
If initial attempts fail, retry with increasingly slower digit spacing, then resort to spoken fallback when DTMF fails consistently.

**Test Multiple Providers**
The documentation suggests comparing Twilio, Telnyx, Vonage, Vapi Numbers, and BYOK SIP transports since "DTMF sending varies across telephony providers."

**Combined Key Entry**
For multiple-digit sequences, send them simultaneously with pause characters rather than separate calls, as "Multiple separate `dtmf` calls can arrive too slowly."

## Smart Endpointing
LiveKit's `startSpeakingPlan` configuration allows slower response cadence during IVR interaction and faster responses once humans answer.
