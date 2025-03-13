import { applyCategories } from '../../utils';
import type { Category, Product } from '../../types';

describe('applyCategories', () => {
    const products: Product[] = [
        { id: 1, name: 'iPhone', description: 'Смартфон', price: 1000, priceSymbol: '$', category: 'Электроника' },
        { id: 2, name: 'Куртка', description: 'Тёплая куртка', price: 200, priceSymbol: '$', category: 'Одежда' },
        { id: 3, name: 'Наушники', description: 'Беспроводные', price: 150, priceSymbol: '$', category: 'Электроника' },
    ];

    test('возвращает все товары, если категории не выбраны', () => {
        expect(applyCategories(products, [])).toEqual(products);
    });

    test('фильтрует товары по одной категории', () => {
        expect(applyCategories(products, ['Электроника'])).toEqual([
            { id: 1, name: 'iPhone', description: 'Смартфон', price: 1000, priceSymbol: '$', category: 'Электроника' },
            { id: 3, name: 'Наушники', description: 'Беспроводные', price: 150, priceSymbol: '$', category: 'Электроника' },
        ]);
    });

    test('фильтрует товары по нескольким категориям', () => {
        expect(applyCategories(products, ['Электроника', 'Одежда'])).toEqual(products);
    });
});
