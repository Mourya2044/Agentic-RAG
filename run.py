from app.core.config import get_settings

settings = get_settings()

print(f"App Name: {settings.app_name}")
print(f"App Environment: {settings.app_env}")
print(f"Audit DB Path: {settings.audit_db_path}")
print(f"Uploads Directory: {settings.uploads_dir}")
print(f"Sample Knowledge Base Directory: {settings.sample_kb_dir}")