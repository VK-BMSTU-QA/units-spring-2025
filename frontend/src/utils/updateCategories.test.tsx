import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { updateCategories } from './updateCategories';
afterEach(jest.clearAllMocks);
import type { Category } from '../types';


describe("UpdateCategories testing", () => {
    it("Check update with two", () => {
        const currentCategories: Category[] = ['Одежда', 'Электроника']
        const changedCategories = 'Одежда'
        expect(updateCategories(currentCategories, changedCategories)).toBe(['Электроника']);
    })
    it("Check update with three", () => {
        const currentCategories: Category[] = ['Одежда', 'Электроника']
        const changedCategories = 'Для дома'
        expect(updateCategories(currentCategories, changedCategories)).toBe([]);
    })
    it("Check update without", () => {
        const currentCategories: Category[] = []
        const changedCategories = 'Для дома'
        expect(updateCategories(currentCategories, changedCategories)).toBe(['Для дома']);
    })
    it("Check update with one delete", () => {
        const currentCategories: Category[] = ['Для дома']
        const changedCategories = 'Для дома'
        expect(updateCategories(currentCategories, changedCategories)).toBe([]);
    })
    it("Check update with one create", () => {
        const currentCategories: Category[] = ['Для дома']
        const changedCategories = 'Электроника'
        expect(updateCategories(currentCategories, changedCategories)).toBe(['Для дома', 'Электроника']);
    })
})