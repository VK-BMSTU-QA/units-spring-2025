import { getPrice } from '../getPrice';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(getPrice(100, '₽')).toBe('100 ₽');
        expect(getPrice(325, '$')).toBe('325 $');
        expect(getPrice(325.4566666666666, '$')).toBe('325,457 $');
        expect(getPrice(300)).toBe('300 ₽');
    });

    it('should return value without price symbol', () => {
        expect(getPrice(300)).toBe('300 ₽');
    });

    it('should round up to 3 decimal places for a fractional value', () => {
        expect(getPrice(325.4566666666666, '$')).toBe('325,457 $');
    });

    it('should missing a negative price', () => {
        expect(getPrice(-325, '$')).toBe('-325 $');
    });
});
