import { getPrice } from '../getPrice';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(getPrice(100, '₽')).toBe('100 ₽');
        expect(getPrice(325, '$')).toBe('325 $');
    });

    // Тест с дробной ценой
    it('should handle fractional price correctly', () => {
        expect(getPrice(99.99, '₽')).toBe('99,99 ₽');
        expect(getPrice(199.95, '$')).toBe('199,95 $');
    });

    // Тест с пустым символом валюты
    it('should handle empty currency symbol correctly', () => {
        expect(getPrice(100)).toBe('100 ');
    });

    // Тест с отсутствующим символом валюты (undefined или null)
    it('should handle undefined or null currency symbol correctly', () => {
        expect(getPrice(100, undefined)).toBe('100 ');
        expect(getPrice(100)).toBe('100 ');
    });

    // Тест с большими числами
    it('should handle large numbers correctly', () => {
        expect(getPrice(1000000, '₽')).toBe('1 000 000 ₽');
        expect(getPrice(9999999, '$')).toBe('9999999 $');
    });
});
