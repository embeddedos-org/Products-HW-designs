import 'package:dio/dio.dart';

class ApiService {
  static const String _baseUrl = 'https://api.americangroupllc.com/v1/eradar360';
  late final Dio _dio;

  ApiService() {
    _dio = Dio(BaseOptions(
      baseUrl: _baseUrl,
      connectTimeout: const Duration(seconds: 15),
      receiveTimeout: const Duration(seconds: 30),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-App-ID': 'eradar360',
      },
    ));
    _dio.interceptors.add(InterceptorsWrapper(
      onError: (DioException e, handler) {
        // Graceful error handling — surface user-friendly messages
        handler.next(e);
      },
    ));
  }

  Future<Response> get(String path, {Map<String, dynamic>? params}) =>
      _dio.get(path, queryParameters: params);

  Future<Response> post(String path, {dynamic data}) =>
      _dio.post(path, data: data);

  Future<Response> put(String path, {dynamic data}) =>
      _dio.put(path, data: data);

  Future<Response> delete(String path) => _dio.delete(path);
}
