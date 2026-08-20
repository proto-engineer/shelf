"""
Seed catalogue.

Each entry is (name, domain, free_tier, icon, use[, href]).
- domain      -> the fallback link, and the logo lookup
- free_tier   -> True if there's a usable free plan (not just a trial)
- icon        -> Simple Icons slug for the real brand logo. "" = fall back.
- use         -> one short line: what you'd actually use it for
- href        -> optional deep link (program/application page). Public URLs
                 only — never workspace pages or links with auth/tracking IDs.
Order inside each category is free-first.
"""

CATALOG = [
    {
        "slug": "assistants",
        "name": "Assistants",
        "kind": "Ask anything, get answers",
        "tools": [
            ("ChatGPT",    "chatgpt.com",       True,  "openai",       "Everyday questions and writing"),
            ("Claude",     "claude.ai",         True,  "claude",       "Deep reasoning, long documents"),
            ("Gemini",     "gemini.google.com", True,  "googlegemini", "Google-connected answers"),
            ("DeepSeek",   "deepseek.com",      True,  "deepseek",     "Strong reasoning, fully free"),
            ("Perplexity", "perplexity.ai",     True,  "perplexity",   "Answers with cited sources"),
            ("Grok",       "grok.com",          True,  "grok",         "Real-time X knowledge"),
            ("Mistral",    "mistral.ai",        True,  "mistralai",    "Open European models"),
        ],
    },
    {
        "slug": "coding",
        "name": "Coding",
        "kind": "Write and fix code",
        "tools": [
            ("Cline",       "cline.bot",    True,  "",              "Open-source agent in VS Code"),
            ("Copilot",     "github.com",   True,  "githubcopilot", "Autocomplete in your editor"),
            ("Windsurf",    "windsurf.com", True,  "",              "Agentic code editor"),
            ("Cursor",      "cursor.com",   True,  "",              "AI-first code editor"),
            ("Bolt",        "bolt.new",     True,  "",              "Full apps in the browser"),
            ("Lovable",     "lovable.dev",  True,  "",              "Idea to web app"),
            ("v0",          "v0.app",       True,  "vercel",        "UI from a prompt"),
            ("Claude Code", "claude.com",   False, "claude",        "Terminal coding agent"),
        ],
    },
    {
        "slug": "video",
        "name": "Video & image",
        "kind": "Make pictures and videos",
        "tools": [
            ("Krea",       "krea.ai",        True,  "",           "Real-time image playground"),
            ("Leonardo",   "leonardo.ai",    True,  "",           "Game art and illustrations"),
            ("Kling",      "klingai.com",    True,  "",           "Text to video"),
            ("Freepik",    "freepik.com",    True,  "freepik",    "AI plus stock assets"),
            ("Runway",     "runwayml.com",   True,  "",           "Pro AI video editing"),
            ("Flow",       "labs.google",    False, "",           "Cinematic scenes by Google"),
            ("Midjourney", "midjourney.com", False, "midjourney", "Best-in-class images"),
        ],
    },
    {
        "slug": "voice",
        "name": "Voice & audio",
        "kind": "Make speech and music",
        "tools": [
            ("ElevenLabs", "elevenlabs.io", True, "elevenlabs", "Lifelike text to speech"),
            ("Deepgram",   "deepgram.com",  True, "",           "Fast transcription API"),
            ("Suno",       "suno.com",      True, "",           "Full songs from a prompt"),
            ("Murf",       "murf.ai",       True, "",           "Voiceovers for videos"),
            ("Cartesia",   "cartesia.ai",   True, "",           "Low-latency voice API"),
            ("PlayHT",     "play.ht",       True, "",           "Voice cloning"),
        ],
    },
    {
        "slug": "identity",
        "name": "Identity & KYC",
        "kind": "Check someone is a real person",
        "tools": [
            ("Didit",      "didit.me",        True,  "", "Free ID verification"),
            ("Persona",    "withpersona.com", True,  "", "KYC building blocks"),
            ("HyperVerge", "hyperverge.co",   False, "", "India-focused KYC"),
            ("IDfy",       "idfy.com",        False, "", "Background checks, India"),
            ("Signzy",     "signzy.com",      False, "", "Bank-grade onboarding"),
            ("Sumsub",     "sumsub.com",      False, "", "Global KYC and AML"),
            ("Onfido",     "onfido.com",      False, "", "Document + selfie checks"),
            ("Veriff",     "veriff.com",      False, "", "Fast identity checks"),
        ],
    },
    {
        "slug": "otp",
        "name": "OTP & messaging",
        "kind": "Send OTP codes and SMS",
        "tools": [
            ("Firebase Auth", "firebase.google.com", True,  "firebase", "Free phone OTP login"),
            ("Fast2SMS",      "fast2sms.com",        True,  "",         "Cheap Indian SMS"),
            ("2Factor",       "2factor.in",          True,  "",         "Indian OTP API"),
            ("MSG91",         "msg91.com",           False, "",         "OTP + WhatsApp, India"),
            ("Plivo",         "plivo.com",           False, "",         "Global SMS and voice"),
            ("Twilio",        "twilio.com",          False, "twilio",   "The default SMS API"),
            ("Vonage",        "vonage.com",          False, "vonage",   "SMS and verify APIs"),
            ("Infobip",       "infobip.com",         False, "infobip",  "Omnichannel messaging"),
        ],
    },
    {
        "slug": "programs",
        "name": "Startup programs",
        "kind": "Free credits and perks for founders",
        "tools": [
            ("AWS Activate",         "aws.amazon.com",          True, "",            "AWS cloud credits",          "https://aws.amazon.com/startups"),
            ("Google for Startups",  "cloud.google.com",        True, "googlecloud", "GCP credits + Workspace",    "https://cloud.google.com/startup/apply"),
            ("NVIDIA Inception",     "nvidia.com",              True, "nvidia",      "Path to $100K AWS credits",  "https://www.nvidia.com/en-in/startups/"),
            ("MongoDB for Startups", "mongodb.com",             True, "mongodb",     "Atlas credits + advisor",    "https://www.mongodb.com/startups"),
            ("Claude for Startups",  "anthropic.com",           True, "claude",      "Claude API credits",         "https://www.anthropic.com/startups"),
            ("OpenAI Startups",      "openai.com",              True, "openai",      "Builder community + credits","https://openai.com/startups"),
            ("ElevenLabs Grants",    "elevenlabs.io",           True, "elevenlabs",  "Voice API grant",            "https://elevenlabs.io/startup-grants"),
            ("Sentry for Startups",  "sentry.io",               True, "sentry",      "$5K monitoring credits",     "https://sentry.io/for/startups/"),
            ("Cloudflare Startups",  "cloudflare.com",          True, "cloudflare",  "Product credits",            "https://www.cloudflare.com/forstartups/"),
            ("GitLab for Startups",  "gitlab.com",              True, "gitlab",      "Free GitLab Ultimate",       "https://about.gitlab.com/solutions/startups/"),
            ("Retool for Startups",  "retool.com",              True, "",            "Internal-tool credits",      "https://retool.com/startups"),
            ("Persona Startups",     "withpersona.com",         True, "",            "KYC + KYB free tier",        "https://help.withpersona.com/articles/1XNnqukfZY9VamF2e7jkuJ/"),
            ("Signzy Startups",      "signzy.com",              True, "",            "KYC + KYB APIs, India",      "https://www.signzy.com/fintech-apis/startups"),
            ("AssemblyAI Startups",  "assemblyai.com",          True, "assemblyai",  "Speech-to-text credits",     "https://www.assemblyai.com/contact/startup-program"),
            ("Arize for Startups",   "arize.com",               True, "",            "LLM observability + evals",  "https://arize.com/arize-for-startups/"),
            ("Perplexity Startups",  "perplexity.ai",           True, "perplexity",  "API credits + Pro",          "https://www.perplexity.ai/startups"),
            ("DocSend Startups",     "dropbox.com",             True, "dropbox",     "90% off deck sharing",       "https://experience.dropbox.com/docsend/startups"),
            ("Infobip Tribe",        "infobip.com",             True, "infobip",     "Messaging credits",          "https://www.infobip.com/startup-tribe"),
            ("Google Ads credit",    "ads.google.com",          True, "googleads",   "Ad credit after first spend","https://ads.google.com/aw/signup"),
            ("Stripe Atlas",         "stripe.com",              False, "stripe",     "US inc + partner perks",     "https://stripe.com/atlas"),
            ("Azure for Students",   "azure.microsoft.com",     True, "",            "$100 Azure credit",          "https://azure.microsoft.com/free/students"),
        ],
    },
    {
        "slug": "stack",
        "name": "Builder stack",
        "kind": "What we actually build with",
        "tools": [
            ("GitHub",           "github.com",           True,  "github",      "Code hosting"),
            ("Supabase",         "supabase.com",         True,  "supabase",    "Postgres backend"),
            ("Postman",          "postman.com",          True,  "postman",     "API testing"),
            ("Expo",             "expo.dev",             True,  "expo",        "React Native builds"),
            ("Replit",           "replit.com",           True,  "replit",      "Cloud IDE + hosting"),
            ("Bubble",           "bubble.io",            True,  "",            "No-code web apps"),
            ("PostHog",          "posthog.com",          True,  "posthog",     "Product analytics"),
            ("Resend",           "resend.com",           True,  "resend",      "Email API"),
            ("New Relic",        "newrelic.com",         True,  "newrelic",    "App monitoring"),
            ("CodeRabbit",       "coderabbit.ai",        True,  "",            "AI pull-request reviews"),
            ("Notion",           "notion.so",            True,  "notion",      "Docs and wikis"),
            ("Slack",            "slack.com",            True,  "slack",       "Team chat"),
            ("Whimsical",        "whimsical.com",        True,  "",            "Diagrams and wireframes"),
            ("Google AI Studio", "aistudio.google.com",  True,  "",            "Gemini API playground"),
            ("Otter",            "otter.ai",             True,  "",            "Meeting notes"),
            ("Mercury",          "mercury.com",          True,  "",            "Startup banking"),
            ("LaunchDarkly",     "launchdarkly.com",     False, "launchdarkly","Feature flags"),
            ("Razorpay",         "razorpay.com",         False, "razorpay",    "Indian payments"),
        ],
    },
]
