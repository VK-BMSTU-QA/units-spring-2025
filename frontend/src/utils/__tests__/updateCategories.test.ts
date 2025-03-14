import { updateCategories } from '../updateCategories';
import type { Category } from '../../types/Category';

describe('test updateCategories function', () => {
    it('should add a new category if it is not in the list', () => {
        const currentCategories: Category[] = ['Электроника', 'Одежда'];
        const newCategory: Category = 'Мебель';

        const updatedCategories = updateCategories(
            currentCategories,
            newCategory
        );

        expect(updatedCategories).toEqual(['Электроника', 'Одежда', 'Мебель']);
    });

    it('should remove a category if it is already in the list', () => {
        const currentCategories: Category[] = [
            'Электроника',
            'Одежда',
            'Мебель',
        ];
        const existingCategory: Category = 'Одежда';

        const updatedCategories = updateCategories(
            currentCategories,
            existingCategory
        );

        expect(updatedCategories).toEqual(['Электроника', 'Мебель']);
    });

    it('should handle an empty list of categories', () => {
        const currentCategories: Category[] = [];
        const newCategory: Category = 'Электроника';

        const updatedCategories = updateCategories(
            currentCategories,
            newCategory
        );

        expect(updatedCategories).toEqual(['Электроника']);
    });

    it('should handle adding and removing multiple categories', () => {
        let currentCategories: Category[] = ['Электроника', 'Одежда'];

        // Добавляем новую категорию
        currentCategories = updateCategories(currentCategories, 'Мебель');
        expect(currentCategories).toEqual(['Электроника', 'Одежда', 'Мебель']);

        // Удаляем существующую категорию
        currentCategories = updateCategories(currentCategories, 'Одежда');
        expect(currentCategories).toEqual(['Электроника', 'Мебель']);

        // Добавляем ещё одну новую категорию
        currentCategories = updateCategories(currentCategories, 'Книги');
        expect(currentCategories).toEqual(['Электроника', 'Мебель', 'Книги']);
    });
});
