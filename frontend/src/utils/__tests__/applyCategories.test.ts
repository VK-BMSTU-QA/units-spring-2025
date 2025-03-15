import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const products: Product[] = [
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

    it('should return same produtcs if categories are empty', () => {
        expect(applyCategories(products, [])).toStrictEqual(products);
    });

    it('should return all products if all categories are given', () => {
        const allCategories: Category[] = ['Для дома', 'Одежда', 'Электроника'];
        expect(applyCategories(products, allCategories)).toStrictEqual(products);
    });

    it('should return products only with given categories', () => {
        const initialProducts: Product[] = products;
        const categories: Category[] = ['Одежда'];
        const expectedProducts: Product[] = [initialProducts[1]];
        
        expect(applyCategories(initialProducts, categories)).toStrictEqual(expectedProducts);
    });
})
