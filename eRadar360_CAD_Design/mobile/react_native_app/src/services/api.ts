import axios, { AxiosInstance, AxiosResponse } from 'axios';

const BASE_URL = 'https://api.americangroupllc.com/v1';

class ApiService {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: `${BASE_URL}/eradar360_cad`,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-App-Name': 'eRadar360_CAD',
        'X-App-Version': '1.0.0',
      },
    });
    this.client.interceptors.response.use(
      (response: AxiosResponse) => response,
      (error) => {
        console.error('[API Error]', error?.response?.status, error?.message);
        return Promise.reject(error);
      }
    );
  }

  async get<T>(endpoint: string, params?: Record<string, unknown>): Promise<T> {
    const response = await this.client.get<T>(endpoint, { params });
    return response.data;
  }

  async post<T>(endpoint: string, data?: unknown): Promise<T> {
    const response = await this.client.post<T>(endpoint, data);
    return response.data;
  }

  async put<T>(endpoint: string, data?: unknown): Promise<T> {
    const response = await this.client.put<T>(endpoint, data);
    return response.data;
  }

  async delete<T>(endpoint: string): Promise<T> {
    const response = await this.client.delete<T>(endpoint);
    return response.data;
  }
}

export const api = new ApiService();
export default api;
