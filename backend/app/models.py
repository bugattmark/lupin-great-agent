from sqlalchemy import Column, String, Text, Float, Boolean, Integer, DateTime, JSON, func
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(String, primary_key=True, default=generate_uuid)
    content = Column(Text, nullable=False)
    source = Column(String(100))  # 'L1B3RT4S' or 'CL4R1T4S'
    category = Column(String(50))  # 'jailbreak', 'system_prompt', etc.
    subcategory = Column(String(50))
    provider = Column(String(50))  # 'anthropic', 'openai', etc.
    severity = Column(String(20))  # 'low', 'medium', 'high', 'critical'
    success_rate = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    extra_data = Column(JSON)

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(String, primary_key=True, default=generate_uuid)
    session_id = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text)
    success = Column(Boolean, default=False)
    model_name = Column(String(100))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    extra_data = Column(JSON)

class Exploit(Base):
    """CVE-style tracking for prompt injections and exploits"""
    __tablename__ = "exploits"

    id = Column(String, primary_key=True, default=generate_uuid)
    cve_id = Column(String(50), unique=True, nullable=False)  # e.g., PIE-2025-001
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    exploit_content = Column(Text, nullable=False)  # The actual exploit/injection
    exploit_type = Column(String(50))  # 'prompt_injection', 'jailbreak', 'data_extraction', etc.
    severity = Column(String(20))  # 'low', 'medium', 'high', 'critical'
    source = Column(String(200))  # Where it was discovered
    source_type = Column(String(50))  # 'auto_agent', 'manual', 'github', etc.
    target_models = Column(JSON)  # List of models vulnerable to this
    mitigation = Column(Text)  # Mitigation strategies
    status = Column(String(20), default='active')  # 'active', 'patched', 'archived'
    discovered_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    extra_data = Column(JSON)

class TestRun(Base):
    """Regression test runs to track safety metrics over time"""
    __tablename__ = "test_runs"

    id = Column(String, primary_key=True, default=generate_uuid)
    run_name = Column(String(200))
    exploit_id = Column(String, nullable=False)
    target_model = Column(String(100), nullable=False)
    test_prompt = Column(Text, nullable=False)
    response = Column(Text)
    success = Column(Boolean, default=False)
    blocked = Column(Boolean, default=False)
    execution_time_ms = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    extra_data = Column(JSON)

class AIProvider(Base):
    """Contact information for AI model providers for security notifications"""
    __tablename__ = "ai_providers"

    id = Column(String, primary_key=True, default=generate_uuid)
    provider_name = Column(String(100), unique=True, nullable=False)
    company_name = Column(String(200), nullable=False)
    security_email = Column(String(200))
    webhook_url = Column(String(500))
    contact_name = Column(String(200))
    notification_enabled = Column(Boolean, default=True)
    notification_method = Column(String(20), default='email')
    model_patterns = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    extra_data = Column(JSON)

class JailbreakNotification(Base):
    """Log of all jailbreak notifications sent to AI providers"""
    __tablename__ = "jailbreak_notifications"

    id = Column(String, primary_key=True, default=generate_uuid)
    provider_id = Column(String, nullable=False)
    attempt_id = Column(String)
    test_run_id = Column(String)
    exploit_id = Column(String)
    model_name = Column(String(100), nullable=False)
    jailbreak_prompt = Column(Text, nullable=False)
    notification_method = Column(String(20))
    notification_status = Column(String(20), default='pending')
    notification_response = Column(Text)
    sent_at = Column(DateTime(timezone=True), server_default=func.now())
    extra_data = Column(JSON)
