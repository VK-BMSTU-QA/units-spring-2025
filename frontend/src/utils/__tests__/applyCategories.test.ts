import { applyCategories } from '../applyCategories';

describe('test applyCategories', () => {
    it('must filter list', () => {
        expect(applyCategories([{id: 1,
            name: "name",
            description: "description",
            price: 100,
            priceSymbol: '₽',
            category: "Электроника",},
            {id: 1,
                name: "name",
                description: "description",
                price: 100,
                priceSymbol: '₽',
                category: "Одежда",}], ["Электроника"])
        ).toStrictEqual([{
            id: 1,
            name: "name",
            description: "description",
            price: 100,
            priceSymbol: '₽',
            category: "Электроника",
        }]);
    });

    it('should return empty', () => {
        expect(applyCategories([], ["Электроника"])
        ).toStrictEqual([]);
    });
});