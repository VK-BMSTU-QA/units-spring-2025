import { applyCategories } from '../applyCategories';
import type { Category, Product, PriceSymbol } from '../../types';

const products = [{
    id: 1,
    name: 'string',
    description: 'string',
    price: 2,
    priceSymbol: '₽' as PriceSymbol,
    imgUrl: 'string',
    category: 'Одежда' as Category
}]

const categories = ['Электроника']

describe('test apply category function', () => {
    it('should return value with price symbol', () => {
        expect(applyCategories(products, categories as Category[])).toBe({
    id: 1,
    name: 'string',
    description: 'string',
    price: 2,
    priceSymbol: '₽' as PriceSymbol,
    imgUrl: 'string',
    category: 'Электроника' as Category
});
    });
    it('should return value with price symbol', () => {
        expect(applyCategories(products, [] as Category[])).toBe({
    id: 1,
    name: 'string',
    description: 'string',
    price: 2,
    priceSymbol: '₽' as PriceSymbol,
    imgUrl: 'string',
    category: 'Одежда' as Category
});
    });
});

