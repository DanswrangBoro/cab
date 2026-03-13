from fastapi import FastAPI
from app.driver.routers.auth import router as driver_auth_router
from app.driver.routers.registration import router as driver_registration_router
from app.rider.routers.auth import router as rider_auth_router
from app.rider.routers.registration import router as rider_registration_router


app = FastAPI(
    title="Ride API",
    description="Backend for Rider and Driver services",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"message": "Ride API is running successfully"}

# Driver routes
app.include_router(driver_registration_router)
app.include_router(driver_auth_router)

# Rider routes
app.include_router(rider_registration_router)
app.include_router(rider_auth_router)
