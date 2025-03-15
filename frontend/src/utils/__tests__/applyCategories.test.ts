import { applyCategories } from '../applyCategories';


describe('test update categories function', () => {
    it('should return product by categories', () => {
        expect(applyCategories([
            { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
            { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
        ], ['Одежда'])).
            toStrictEqual([{ id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' }])

        expect(applyCategories([
            { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
            { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
        ], ['Одежда', 'Электроника'])).
            toStrictEqual([{ id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' }])

        expect(applyCategories([
            { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
            { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
            { id: 3, description: 'Комп', category: 'Электроника', price: 100, name: 'third name' },
        ], [])).
            toStrictEqual([
                { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
                { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
                { id: 3, description: 'Комп', category: 'Электроника', price: 100, name: 'third name' },
            ])

        expect(applyCategories([
            { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
            { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
            { id: 3, description: 'Комп', category: 'Электроника', price: 100, name: 'third name' },
        ], ['Электроника', 'Одежда', 'Для дома'])).
            toStrictEqual([
                { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' },
                { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' },
                { id: 3, description: 'Комп', category: 'Электроника', price: 100, name: 'third name' },
            ])

    });
});