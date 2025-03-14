import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('returns only those products that have product.category in the passed category list', () => {
        const products: Product[] = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                imgUrl: '/iphone.png',
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
                priceSymbol: '₽',
                imgUrl: '/lamp.png',
                category: 'Для дома',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                priceSymbol: '₽',
                category: 'Электроника',
            },
        ];

        const expected = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                imgUrl: '/iphone.png',
                category: 'Электроника',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                priceSymbol: '₽',
                category: 'Электроника',
            },
        ];

        const actual = applyCategories(products, ['Электроника']);
        expect(actual).toEqual(expected);
    });
});
