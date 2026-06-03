/**
 * Production-ready GPS Location Integration Service.
 * Automatically resolves coordinates via navigator.geolocation or fallback IP-Geolocation API.
 */
export interface GPSCoordinates {
  latitude: number;
  longitude: number;
  accuracy?: number;
  provider: 'device' | 'ip_fallback' | 'default';
}

export async function getCurrentLocation(): Promise<GPSCoordinates> {
  if (typeof navigator !== 'undefined' && navigator.geolocation) {
    try {
      const position = await new Promise<GeolocationPosition>((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject, {
          enableHighAccuracy: true,
          timeout: 5000,
          maximumAge: 0
        });
      });
      return {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
        accuracy: position.coords.accuracy,
        provider: 'device'
      };
    } catch (e) {
      console.warn("Device GPS failed, falling back to IP Geolocation:", e);
    }
  }

  try {
    const response = await fetch('https://ipapi.co/json/');
    if (response.ok) {
      const data = await response.json();
      return {
        latitude: data.latitude || 37.7749,
        longitude: data.longitude || -122.4194,
        provider: 'ip_fallback'
      };
    }
  } catch (e) {
    console.error("IP Geolocation fallback failed:", e);
  }

  return {
    latitude: 37.7749,
    longitude: -122.4194,
    provider: 'default'
  };
}
