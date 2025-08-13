from fastapi import APIRouter

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])

@router.get("/about")
def get_about():
    return {
        "name": "Your Name",
        "role": "Python & FastAPI Developer",
        "experience": "10 years",
        "skills": ["Python", "FastAPI", "JavaScript", "Vue3", "AWS"]
    }

@router.get("/skills")
def get_skills():
    return {
        "technical": ["Python", "JavaScript", "Vue3", "FastAPI", "AWS"],
        "soft": ["Communication", "Problem Solving", "Teamwork"]
    }
