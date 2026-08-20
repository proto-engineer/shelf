"""
Seed catalogue.

Each entry is (name, domain, free_tier, icon).
- domain      -> the link, and the fallback logo lookup
- free_tier   -> True if there's a usable free plan (not just a trial)
- icon        -> Simple Icons slug for the real brand logo. "" = fall back.
Order inside each category is free-first.
"""

CATALOG = [
    {
        "slug": "assistants",
        "name": "Assistants",
        "kind": "Ask anything, get answers",
        "tools": [
            ("ChatGPT",    "chatgpt.com",       True,  "openai"),
            ("Claude",     "claude.ai",         True,  "claude"),
            ("Gemini",     "gemini.google.com", True,  "googlegemini"),
            ("DeepSeek",   "deepseek.com",      True,  "deepseek"),
            ("Perplexity", "perplexity.ai",     True,  "perplexity"),
            ("Grok",       "grok.com",          True,  "grok"),
            ("Mistral",    "mistral.ai",        True,  "mistralai"),
        ],
    },
    {
        "slug": "coding",
        "name": "Coding",
        "kind": "Write and fix code",
        "tools": [
            ("Cline",       "cline.bot",    True,  ""),
            ("Copilot",     "github.com",   True,  "githubcopilot"),
            ("Windsurf",    "windsurf.com", True,  ""),
            ("Cursor",      "cursor.com",   True,  ""),
            ("Bolt",        "bolt.new",     True,  ""),
            ("Lovable",     "lovable.dev",  True,  ""),
            ("v0",          "v0.app",       True,  "vercel"),
            ("Claude Code", "claude.com",   False, "claude"),
        ],
    },
    {
        "slug": "video",
        "name": "Video & image",
        "kind": "Make pictures and videos",
        "tools": [
            ("Krea",       "krea.ai",        True,  ""),
            ("Leonardo",   "leonardo.ai",    True,  ""),
            ("Kling",      "klingai.com",    True,  ""),
            ("Freepik",    "freepik.com",    True,  "freepik"),
            ("Runway",     "runwayml.com",   True,  ""),
            ("Flow",       "labs.google",    False, ""),
            ("Midjourney", "midjourney.com", False, "midjourney"),
        ],
    },
    {
        "slug": "voice",
        "name": "Voice & audio",
        "kind": "Make speech and music",
        "tools": [
            ("ElevenLabs", "elevenlabs.io", True, "elevenlabs"),
            ("Deepgram",   "deepgram.com",  True, ""),
            ("Suno",       "suno.com",      True, ""),
            ("Murf",       "murf.ai",       True, ""),
            ("Cartesia",   "cartesia.ai",   True, ""),
            ("PlayHT",     "play.ht",       True, ""),
        ],
    },
    {
        "slug": "identity",
        "name": "Identity & KYC",
        "kind": "Check someone is a real person",
        "tools": [
            ("Didit",      "didit.me",        True,  ""),
            ("Persona",    "withpersona.com", True,  ""),
            ("HyperVerge", "hyperverge.co",   False, ""),
            ("IDfy",       "idfy.com",        False, ""),
            ("Signzy",     "signzy.com",      False, ""),
            ("Sumsub",     "sumsub.com",      False, ""),
            ("Onfido",     "onfido.com",      False, ""),
            ("Veriff",     "veriff.com",      False, ""),
        ],
    },
    {
        "slug": "otp",
        "name": "OTP & messaging",
        "kind": "Send OTP codes and SMS",
        "tools": [
            ("Firebase Auth", "firebase.google.com", True,  "firebase"),
            ("Fast2SMS",      "fast2sms.com",        True,  ""),
            ("2Factor",       "2factor.in",          True,  ""),
            ("MSG91",         "msg91.com",           False, ""),
            ("Plivo",         "plivo.com",           False, ""),
            ("Twilio",        "twilio.com",          False, "twilio"),
            ("Vonage",        "vonage.com",          False, "vonage"),
            ("Infobip",       "infobip.com",         False, "infobip"),
        ],
    },
]
