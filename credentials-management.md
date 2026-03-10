
# 🔐 Credentials & API Key Management

*Research Date: 2026-03-10*
*Purpose: Optimal method for Jarvis to access credentials*

---

## Current Setup Analysis

- OpenClaw running in Docker container
- GitHub repos for storage
- OpenRouter API key needed
- Potential: Grok API, 1Password, Codex CLI

---

## Options Researched

### 1. Environment Variables (Recommended for Docker)
**Pros:**
- Standard Docker practice
- Easy to manage via docker-compose
- No code changes needed

**Cons:**
- Need to restart container on changes
- Visible in process list if not careful

**How:**
```bash
# In docker-compose or run command
-e OPENROUTER_API_KEY=xxx
-e GROK_API_KEY=xxx
```

---

### 2. OpenClaw Config File
**Pros:**
- Built into the system
- Already used for some keys
- Accessible to all agents

**Cons:**
- May not be encrypted
- Needs manual editing

**Location:** `~/.openclaw/openclaw.json`

---

### 3. Encrypted File (Future)
**Pros:**
- Secure at rest
- Version control friendly (encrypted)

**Cons:**
- Need encryption/decryption step
- More complex setup

---

### 4. External Secrets Manager (1Password)
**Pros:**
- Professional grade
- Already have 1Password CLI
- Secure

**Cons:**
- Need to install CLI in container
- More setup

---

## Recommended Approach

### Phase 1: Environment Variables (Now)
- Store in Docker config
- Add to docker-compose.yaml
- Use for: OpenRouter, Grok

### Phase 2: OpenClaw Config
- Update existing config with new keys
- Document in TOOLS.md

### Phase 3: 1Password (Later)
- Install 1Password CLI
- Use for sensitive credentials

---

## Action Items

1. [ ] Add API keys to docker-compose environment
2. [ ] Document all keys in TOOLS.md (encrypted references only)
3. [ ] Install 1Password CLI in container (if possible)
4. [ ] Create credential reference system

---

## Keys Needed

| Key | Source | Status |
|-----|--------|--------|
| OpenRouter | Already have | ⚠️ Need valid key |
| Grok API | x.ai/api | Need to get |
| 1Password CLI | brew | Need to install |
| Codex CLI | npm | Need to install |

---

*This guides credential management for Jarvis*
