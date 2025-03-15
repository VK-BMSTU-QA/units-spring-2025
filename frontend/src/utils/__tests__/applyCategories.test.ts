import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {

    const products : Product[] = [
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
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    const category1 : Category = "Одежда";
    const category2 : Category = "Электроника";
    const category3 : Category = "Для дома";

    it('should return products without filter', () => {
        const productsFiltered = applyCategories(products, []);
        expect(productsFiltered).toBe(products);
    });

    it('should return products filtered by one filter', () => {
        const productsFiltered = applyCategories(products, [category1]);
        productsFiltered.forEach((product) => {
            expect(product.category).toBe(category1);
        })
    });

    it('should return products filtered by multiple filters', () => {
        let productsFiltered = applyCategories(products, [category1, category2]);
        productsFiltered.forEach((product) => {
            expect([category1, category2]).toContain(product.category);
        })

        productsFiltered = applyCategories(products, [category2, category3]);
        productsFiltered.forEach((product) => {
            expect([category2, category3]).toContain(product.category);
        })
    });

    it('should return products filtered by all filters', () => {
        const productsFiltered = applyCategories(products, [category1, category2, category3]);
        productsFiltered.forEach((product) => {
            expect([category1, category2, category3]).toContain(product.category);
        })
    });
});