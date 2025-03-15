import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('applyCategories test', () => {
    let products: Product[];

    beforeEach(() => {
        products = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ];
    });

    it('should filter products by one category (Электроника)', () => {
        const categories: Category[] = ['Электроника'];
        const result = applyCategories(products, categories);

        expect(result).toHaveLength(2);
        expect(result).toEqual([products[0], products[3]]);
    });

    it('should filter products by multiple categories (Электроника, Одежда)', () => {
        const categories: Category[] = ['Электроника', 'Одежда'];
        const result = applyCategories(products, categories);

        expect(result).toHaveLength(3);
        expect(result).toEqual([products[0], products[1], products[3]]);
    });

    it('should return all products if all categories are selected', () => {
        const categories: Category[] = ['Электроника', 'Одежда', 'Для дома'];
        const result = applyCategories(products, categories);

        expect(result).toHaveLength(4);
        expect(result).toEqual(products);
    });

    it('should return all products if no categories are selected', () => {
        const categories: Category[] = [];
        const result = applyCategories(products, categories);

        expect(result).toHaveLength(4);
        expect(result).toEqual(products);
    });

    it('should return empty array if no products match the selected categories', () => {
        const categories: Category[] = ['Одежда', 'Электроника'];
        const filteredProducts = products.filter(
            (p) => p.category === 'Для дома'
        );
        const result = applyCategories(filteredProducts, categories);

        expect(result).toHaveLength(0);
        expect(result).toEqual([]);
    });
});
