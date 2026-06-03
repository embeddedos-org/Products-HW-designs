// eRadar360_CAD — Domain Logic Tests

const isValidEmail = (e: string) => /^[\w.+-]+@[\w-]+\.[\w.]+$/.test(e);
const isValidUrl = (u: string) => u.startsWith('http://') || u.startsWith('https://');
const formatCurrency = (amount: number, symbol = '$') => symbol + amount.toFixed(2);
const formatDate = (d: Date) => d.toISOString().split('T')[0];
const clamp = (v: number, min: number, max: number) => Math.min(Math.max(v, min), max);
const truncate = (s: string, max: number) => s.length <= max ? s : s.slice(0, max) + '...';
const paginate = <T>(items: T[], page: number, size: number) => items.slice(page * size, (page + 1) * size);
const toSlug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const daysBetween = (a: Date, b: Date) => Math.abs(Math.round((b.getTime() - a.getTime()) / 86400000));
const isPastDate = (d: Date) => d < new Date();
const deepEqual = (a: any, b: any) => JSON.stringify(a) === JSON.stringify(b);

describe('eRadar360_CAD — Domain Tests', () => {

  describe('Email validation', () => {
    test('valid email', () => expect(isValidEmail('user@example.com')).toBe(true));
    test('invalid — no @', () => expect(isValidEmail('userexample.com')).toBe(false));
    test('invalid — no domain', () => expect(isValidEmail('user@')).toBe(false));
    test('empty string', () => expect(isValidEmail('')).toBe(false));
    test('subdomain email', () => expect(isValidEmail('u@mail.example.co.uk')).toBe(true));
  });

  describe('URL validation', () => {
    test('https valid', () => expect(isValidUrl('https://api.americangroupllc.com')).toBe(true));
    test('http valid', () => expect(isValidUrl('http://localhost:3000')).toBe(true));
    test('ftp invalid', () => expect(isValidUrl('ftp://files.example.com')).toBe(false));
    test('empty invalid', () => expect(isValidUrl('')).toBe(false));
  });

  describe('Currency formatting', () => {
    test('USD', () => expect(formatCurrency(9.99)).toBe('$9.99'));
    test('EUR', () => expect(formatCurrency(5.0, '\u20ac')).toBe('\u20ac5.00'));
    test('zero', () => expect(formatCurrency(0)).toBe('$0.00'));
    test('large amount', () => expect(formatCurrency(99999.99)).toBe('$99999.99'));
    test('rounds to 2dp', () => expect(formatCurrency(1.999)).toBe('$2.00'));
  });

  describe('Date utilities', () => {
    test('format ISO date', () => expect(formatDate(new Date('2026-05-28'))).toBe('2026-05-28'));
    test('days between', () => expect(daysBetween(new Date('2026-01-01'), new Date('2026-01-11'))).toBe(10));
    test('symmetric days', () => expect(daysBetween(new Date('2026-01-11'), new Date('2026-01-01'))).toBe(10));
    test('same day = 0', () => expect(daysBetween(new Date('2026-05-28'), new Date('2026-05-28'))).toBe(0));
    test('past date', () => expect(isPastDate(new Date('2020-01-01'))).toBe(true));
    test('future date', () => expect(isPastDate(new Date('2099-01-01'))).toBe(false));
  });

  describe('Value clamping', () => {
    test('within range', () => expect(clamp(5, 0, 10)).toBe(5));
    test('below min', () => expect(clamp(-1, 0, 10)).toBe(0));
    test('above max', () => expect(clamp(15, 0, 10)).toBe(10));
    test('at min', () => expect(clamp(0, 0, 10)).toBe(0));
    test('at max', () => expect(clamp(10, 0, 10)).toBe(10));
  });

  describe('Text utilities', () => {
    test('truncate long', () => expect(truncate('hello world', 5)).toBe('hello...'));
    test('truncate short', () => expect(truncate('hi', 10)).toBe('hi'));
    test('slug basic', () => expect(toSlug('Hello World')).toBe('hello-world'));
    test('slug special chars', () => expect(toSlug('C++ & Java!')).toBe('c-java'));
    test('slug numbers', () => expect(toSlug('App v2.0')).toBe('app-v2-0'));
  });

  describe('Pagination', () => {
    const items = Array.from({ length: 25 }, (_, i) => i);
    test('first page', () => expect(paginate(items, 0, 10)).toEqual([0,1,2,3,4,5,6,7,8,9]));
    test('second page', () => expect(paginate(items, 1, 10)).toEqual([10,11,12,13,14,15,16,17,18,19]));
    test('last partial', () => expect(paginate(items, 2, 10)).toEqual([20,21,22,23,24]));
    test('out of range', () => expect(paginate(items, 5, 10)).toEqual([]));
    test('empty list', () => expect(paginate([], 0, 10)).toEqual([]));
  });

  describe('Deep equality', () => {
    test('equal objects', () => expect(deepEqual({a:1,b:2},{a:1,b:2})).toBe(true));
    test('unequal objects', () => expect(deepEqual({a:1},{a:2})).toBe(false));
    test('equal arrays', () => expect(deepEqual([1,2,3],[1,2,3])).toBe(true));
    test('nested equal', () => expect(deepEqual({a:{b:1}},{a:{b:1}})).toBe(true));
  });

  describe('Performance', () => {
    test('paginate 10k items 100x under 50ms', () => {
      const large = Array.from({ length: 10000 }, (_, i) => i);
      const start = Date.now();
      for (let i = 0; i < 100; i++) paginate(large, i % 100, 100);
      expect(Date.now() - start).toBeLessThan(50);
    });
    test('slug 1k times under 20ms', () => {
      const start = Date.now();
      for (let i = 0; i < 1000; i++) toSlug('Hello World ' + i);
      expect(Date.now() - start).toBeLessThan(20);
    });
  });
});
