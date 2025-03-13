import { updateCategories } from '../updateCategories';

describe('test updateCategories', () => {
    it('should delet one', () => {
        expect(updateCategories(["Электроника", "Для дома"], "Электроника")).toStrictEqual(["Для дома"]);
    });
    it('should return the same', () => {
        expect(updateCategories(["Электроника", "Для дома"], "Одежда")).toStrictEqual(["Электроника", "Для дома", "Одежда"]);
    });
});