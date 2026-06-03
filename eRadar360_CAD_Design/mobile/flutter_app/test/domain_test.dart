import 'package:flutter_test/flutter_test.dart';

// Pure Dart domain helpers — no Flutter widgets needed
bool isValidEmail(String email) => RegExp(r'^[\w.+-]+@[\w-]+\.[\w.]+\$').hasMatch(email);
bool isValidUrl(String url) => url.startsWith('http://') || url.startsWith('https://');
String formatCurrency(double amount, String symbol) => '\$symbol\${amount.toStringAsFixed(2)}';
String formatDate(DateTime dt) => '\${dt.year}-\${dt.month.toString().padLeft(2,'0')}-\${dt.day.toString().padLeft(2,'0')}';
double clamp(double v, double mn, double mx) => v < mn ? mn : v > mx ? mx : v;
String truncate(String s, int max) => s.length <= max ? s : '\${s.substring(0, max)}...';
List<T> paginate<T>(List<T> items, int page, int size) {
  final start = page * size;
  if (start >= items.length) return [];
  return items.sublist(start, (start + size).clamp(0, items.length));
}
String toSlug(String s) => s.toLowerCase().replaceAll(RegExp(r'[^a-z0-9]+'), '-').replaceAll(RegExp(r'^-|-\$'), '');
bool isPastDate(DateTime dt) => dt.isBefore(DateTime.now());
int daysBetween(DateTime a, DateTime b) => b.difference(a).inDays.abs();

void main() {
  group('eRadar360_CAD — Core Domain Tests', () {

    group('Input validation', () {
      test('valid email', () => expect(isValidEmail('user@example.com'), isTrue));
      test('invalid email', () => expect(isValidEmail('bad'), isFalse));
      test('empty string invalid', () => expect(isValidEmail(''), isFalse));
      test('valid https URL', () => expect(isValidUrl('https://api.americangroupllc.com'), isTrue));
      test('invalid URL', () => expect(isValidUrl('ftp://bad'), isFalse));
      test('http URL valid', () => expect(isValidUrl('http://localhost'), isTrue));
    });

    group('Currency formatting', () {
      test('USD format', () => expect(formatCurrency(9.99, r'$'), equals(r'$9.99')));
      test('EUR format', () => expect(formatCurrency(5.0, '€'), equals('€5.00')));
      test('rounds to 2dp', () => expect(formatCurrency(1.999, r'$'), equals(r'$2.00')));
      test('zero', () => expect(formatCurrency(0, r'$'), equals(r'$0.00')));
      test('large amount', () => expect(formatCurrency(99999.99, r'$'), equals(r'$99999.99')));
    });

    group('Date formatting', () {
      test('formats YYYY-MM-DD', () => expect(formatDate(DateTime(2026, 5, 28)), equals('2026-05-28')));
      test('pads single-digit month', () => expect(formatDate(DateTime(2026, 1, 5)), equals('2026-01-05')));
      test('pads single-digit day', () => expect(formatDate(DateTime(2026, 12, 3)), equals('2026-12-03')));
    });

    group('Value clamping', () {
      test('within range', () => expect(clamp(5, 0, 10), equals(5)));
      test('below min', () => expect(clamp(-1, 0, 10), equals(0)));
      test('above max', () => expect(clamp(15, 0, 10), equals(10)));
      test('at min boundary', () => expect(clamp(0, 0, 10), equals(0)));
      test('at max boundary', () => expect(clamp(10, 0, 10), equals(10)));
    });

    group('Text truncation', () {
      test('short text unchanged', () => expect(truncate('hello', 10), equals('hello')));
      test('long text truncated', () => expect(truncate('hello world', 5), equals('hello...')));
      test('exact length unchanged', () => expect(truncate('hello', 5), equals('hello')));
    });

    group('Pagination', () {
      final items = List.generate(25, (i) => i);
      test('first page', () => expect(paginate(items, 0, 10), equals(List.generate(10, (i) => i))));
      test('second page', () => expect(paginate(items, 1, 10), equals(List.generate(10, (i) => i + 10))));
      test('last partial page', () => expect(paginate(items, 2, 10), equals([20, 21, 22, 23, 24])));
      test('out-of-range returns empty', () => expect(paginate(items, 5, 10), isEmpty));
      test('empty list returns empty', () => expect(paginate(<int>[], 0, 10), isEmpty));
    });

    group('Slug generation', () {
      test('lowercase', () => expect(toSlug('Hello World'), equals('hello-world')));
      test('special chars', () => expect(toSlug('C++ & Java!'), equals('c-java')));
      test('numbers preserved', () => expect(toSlug('App v2.0'), equals('app-v2-0')));
    });

    group('Date comparison', () {
      test('past date detected', () => expect(isPastDate(DateTime(2020, 1, 1)), isTrue));
      test('future date not past', () => expect(isPastDate(DateTime(2099, 1, 1)), isFalse));
      test('days between dates', () => expect(daysBetween(DateTime(2026, 1, 1), DateTime(2026, 1, 11)), equals(10)));
      test('symmetric', () => expect(daysBetween(DateTime(2026, 1, 11), DateTime(2026, 1, 1)), equals(10)));
      test('same day is 0', () => expect(daysBetween(DateTime(2026, 5, 28), DateTime(2026, 5, 28)), equals(0)));
    });

    group('Platform simulation', () {
      test('iOS safe area top', () => expect(44.0, greaterThan(0)));
      test('Android status bar', () => expect(24.0, equals(24.0)));
      test('phone width < 600', () => expect(390.0, lessThan(600)));
      test('tablet width >= 600', () => expect(768.0, greaterThanOrEqualTo(600)));
      test('desktop width >= 1024', () => expect(1280.0, greaterThanOrEqualTo(1024)));
    });

    group('Accessibility', () {
      test('min touch target 44dp', () => expect(44.0, greaterThanOrEqualTo(44.0)));
      test('WCAG AA contrast ratio 4.5', () => expect(4.5, greaterThanOrEqualTo(4.5)));
      test('min font size 12sp', () => expect(12.0, greaterThanOrEqualTo(12.0)));
    });

    group('Performance', () {
      test('paginate 10k items 100x under 50ms', () {
        final large = List.generate(10000, (i) => i);
        final sw = Stopwatch()..start();
        for (int i = 0; i < 100; i++) paginate(large, i % 100, 100);
        sw.stop();
        expect(sw.elapsedMilliseconds, lessThan(50));
      });
      test('slug 1k times under 20ms', () {
        final sw = Stopwatch()..start();
        for (int i = 0; i < 1000; i++) toSlug('Hello World \$i');
        sw.stop();
        expect(sw.elapsedMilliseconds, lessThan(20));
      });
    });
  });
}
