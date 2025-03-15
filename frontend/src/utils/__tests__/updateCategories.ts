import type { Category } from "../../types";
import { updateCategories } from "../updateCategories";

describe('test update categories function', () => {
    const clickedCategory = 'Для дома';
    const emptyCategories: [] = [];
    const oneCategory = ['Для дома'] as Category[];
    const twoCategories = ['Одежда', 'Электроника'] as Category[];
    const threeCategories = ['Для дома', 'Одежда', 'Электроника'] as Category[];

    it('should add clicked category to list of categories if it is not in the list', () => {
        expect(updateCategories(emptyCategories, clickedCategory)).toEqual(oneCategory);
        expect(updateCategories(twoCategories, clickedCategory).sort()).toEqual(threeCategories.sort());
    });

    it('should remove clicked category from list of categories if it was in this list', () => {
        expect(updateCategories(oneCategory, clickedCategory )).toEqual(emptyCategories);
        expect(updateCategories(threeCategories, clickedCategory).sort()).toEqual(twoCategories.sort());
    });
});
