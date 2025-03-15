import { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test applyCategories function', () => {
    const categories: Category[] = ['Для дома', 'Одежда', 'Электроника'];
    const products: Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
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
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    it('should return all products if categories length is 0', () => {
        expect(applyCategories(products, [])).toEqual(products);
    });

    it('shoud return product with selected categories', () => {
        categories.forEach((category) => {
            const expected = products.filter(
                (product) => product.category === category
            );
            expect(applyCategories(products, [category])).toEqual(expected);
        });
        const expected = [products[0], ...products.slice(2, 4)];
        expect(applyCategories(products, ['Для дома', 'Электроника'])).toEqual(
            expected
        );
    });
});
