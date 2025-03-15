import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('test applyCategories function', () => {
    const products: Product[] = [
        // { id: 1, name: 'Телефон', category: 'Электроника', price: 10000 },
        // { id: 2, name: 'Футболка', category: 'Одежда', price: 500 },
        // { id: 3, name: 'Книга', category: 'Книги', price: 300 },
        // { id: 4, name: 'Ноутбук', category: 'Электроника', price: 50000 },
        {
            id: 1001,
            name: 'Mazda',
            description: 'The best Japan auto',
            price: 1999,
            priceSymbol: '$',
            category: 'Электроника',
        },
        {
            id: 1002,
            name: 'BelAZ',
            description: 'The best Belarus auto',
            price: 999999,
            priceSymbol: '₽',
            category: 'Электроника',
        },
        {
            id: 1003,
            name: 'Dodge',
            description: 'The best American auto',
            price: 2999,
            priceSymbol: '$',
            category: 'Электроника',
        },
    ];

    it('should return all products if categories list is empty', () => {
        const categories: Category[] = [];
        const filteredProducts = applyCategories(products, categories);

        expect(filteredProducts).toEqual(products);
    });

    it('should filter products by one category', () => {
        const categories: Category[] = ['Электроника'];
        const filteredProducts = applyCategories(products, categories);

        expect(filteredProducts).toEqual([
            { id: 1, name: 'Телефон', category: 'Электроника', price: 10000 },
            { id: 4, name: 'Ноутбук', category: 'Электроника', price: 50000 },
        ]);
    });

    it('should filter products by multiple categories', () => {
        const categories: Category[] = ['Электроника', 'Одежда'];
        const filteredProducts = applyCategories(products, categories);

        expect(filteredProducts).toEqual([
            { id: 1, name: 'Телефон', category: 'Электроника', price: 10000 },
            { id: 2, name: 'Футболка', category: 'Одежда', price: 500 },
            { id: 4, name: 'Ноутбук', category: 'Электроника', price: 50000 },
        ]);
    });

    it('should return empty array if no products match the categories', () => {
        const categories: Category[] = ['Мебель'];
        const filteredProducts = applyCategories(products, categories);

        expect(filteredProducts).toEqual([]);
    });

    it('should handle empty products list', () => {
        const emptyProducts: Product[] = [];
        const categories: Category[] = ['Электроника'];
        const filteredProducts = applyCategories(emptyProducts, categories);

        expect(filteredProducts).toEqual([]);
    });
});
