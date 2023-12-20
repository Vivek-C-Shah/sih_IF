"""FastAPI app creation, logger configuration and main API routes."""

from fastapi import applications
import llama_index

from private_gpt.di import global_injector
from private_gpt.launcher import create_app
# from private_gpt.server.chat.ocr_router import ocr_router

# applications.include_router(ocr_router)

# Add LlamaIndex simple observability
llama_index.set_global_handler("simple")

app = create_app(global_injector)
