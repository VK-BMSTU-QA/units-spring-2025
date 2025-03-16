import { applyCategories } from '../applyCategories';
import {useProducts} from '../../hooks/useProducts';
import {Category} from '../../types';

const Categories: Category[] = [ 'Электроника'];
const Categories2: Category[] = [ 'Для дома' , 'Одежда'];

const Products = useProducts()

describe('test get price function', () => {
    it('should return filtered products', () => {
        expect(applyCategories(Products, Categories )).toEqual([Products[0], Products[3]]);
    });
    it('should return filtered products', () => {
        expect(applyCategories(Products, Categories2 )).toEqual([Products[1], Products[2]]);
    });
    it('should return filtered products', () => {
        expect(applyCategories(Products, [])).toEqual(Products);
    });
});
