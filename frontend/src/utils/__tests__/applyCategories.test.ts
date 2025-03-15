import type { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

interface TestCase {
    name: string;
    input: {
        products: Product[];
        categories: Category[];
    };
    expectedOutput: Product[];
}

const testCases: TestCase[] = [
    {
        name: 'should return all products if given empty categories',
        input: {
            products: [
                {
                    id: 1,
                    name: 'IPhone 14 Pro',
                    description: 'Latest iphone, buy it now',
                    price: 999,
                    category: 'Электроника',
                },
                {
                    id: 2,
                    name: 'Костюм гуся',
                    description: 'Запускаем гуся, работяги',
                    price: 1000,
                    category: 'Одежда',
                },
                {
                    id: 3,
                    name: 'Настольная лампа',
                    description: 'Говорят, что ее использовали в pixar',
                    price: 699,
                    category: 'Для дома',
                },
            ],
            categories: [],
        },
        expectedOutput: [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                category: 'Одежда',
            },
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
            },
        ],
    },
    {
        name: 'should return empty array if given unused categories',
        input: {
            products: [
                {
                    id: 1,
                    name: 'IPhone 14 Pro',
                    description: 'Latest iphone, buy it now',
                    price: 999,
                    category: 'Электроника',
                },
                {
                    id: 2,
                    name: 'Костюм гуся',
                    description: 'Запускаем гуся, работяги',
                    price: 1000,
                    category: 'Одежда',
                },
            ],
            categories: ['Для дома'],
        },
        expectedOutput: [],
    },
    {
        name: 'should return correct products if given used categories',
        input: {
            products: [
                {
                    id: 1,
                    name: 'IPhone 14 Pro',
                    description: 'Latest iphone, buy it now',
                    price: 999,
                    category: 'Электроника',
                },
                {
                    id: 2,
                    name: 'Костюм гуся',
                    description: 'Запускаем гуся, работяги',
                    price: 1000,
                    category: 'Одежда',
                },
                {
                    id: 3,
                    name: 'Настольная лампа',
                    description: 'Говорят, что ее использовали в pixar',
                    price: 699,
                    category: 'Для дома',
                },
            ],
            categories: ['Электроника', 'Одежда'],
        },
        expectedOutput: [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                category: 'Одежда',
            },
        ],
    },
];

describe('test apply categories function', () => {
    testCases.forEach(({ name, input, expectedOutput }) => {
        it(name, () => {
            expect(applyCategories(input.products, input.categories)).toEqual(
                expectedOutput
            );
        });
    });
});
