import { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

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

    type TestCase = {
        products: Product[];
        categories: Category[];
        expected: Product[];
    };
    
    const testCases: TestCase[] = [
        {
            products,
            categories: [],
            expected: products,
        },
        {
            products,
            categories: ['Электроника'],
            expected: [products[0], products[3]],
        },
        {
            products,
            categories: ['Электроника', 'Одежда'],
            expected: [products[0], products[1], products[3]],
        },
        {
            products,
            categories: ['Одежда'],
            expected: [products[1]],
        },
    ];
    
    test.each<TestCase>(testCases)('applyCategories(%s, %s)', ({ products, categories, expected }) => {
        expect(applyCategories(products as Product[], categories as Category[])).toStrictEqual(expected);
    });
});
