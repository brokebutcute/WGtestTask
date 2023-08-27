from dataclasses import dataclass


@dataclass
class WebsitePopularity:
    website_name: str
    popularity: int
    frontend_language: str
    backend_language: str
