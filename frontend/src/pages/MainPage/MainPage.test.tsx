import React from 'react';
import '@testing-library/jest-dom';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { Category, Product } from '../../types';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        { id: 1, name: 'Принтер', category: 'Электроника' } as Product,
        { id: 2, name: 'Костюм гуся', category: 'Одежда' } as Product,
        { id: 3, name: 'Настольная лампа', category: 'Для дома' } as Product,
    ]),
    useCurrentTime: jest.fn(() => '01:00:00'),
}));

jest.mock('../../utils', () => ({
    getPrice: jest.fn(),
    applyCategories: (products: Product[], categories: Category[]) =>
        categories.length ? products.filter((product: Product) => categories.includes(product.category)) : products,
    updateCategories: (currentCategories: Category[], changedCategories: Category) =>
        currentCategories.includes(changedCategories) ? currentCategories.filter((c: Category) => c !== changedCategories) : [...currentCategories, changedCategories],
}));

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display current time', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('01:00:00')).toBeInTheDocument();
    });

    it('should display all categories', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getAllByText('Электроника')).toHaveLength(2);
        expect(rendered.getAllByText('Для дома')).toHaveLength(2);
        expect(rendered.getAllByText('Одежда')).toHaveLength(2);
    });

    it('should display product cards with one selected category', () => {
        const rendered = render(<MainPage />);

        const categoryBadge = rendered.getAllByText('Одежда')[0];
        fireEvent.click(categoryBadge);

        expect(rendered.getByText('Костюм гуся')).toBeInTheDocument();
        expect(rendered.queryByText('Принтер')).not.toBeInTheDocument();
    });

    it('should display product cards with multiple selected categories', () => {
        const rendered = render(<MainPage />);

        const clothesCategoryBadge = rendered.getAllByText('Одежда')[0];
        const homeCategoryBadge = rendered.getAllByText('Для дома')[0];
        fireEvent.click(clothesCategoryBadge);
        fireEvent.click(homeCategoryBadge);

        expect(rendered.getByText('Костюм гуся')).toBeInTheDocument();
        expect(rendered.getByText('Настольная лампа')).toBeInTheDocument();
        expect(rendered.queryByText('Принтер')).not.toBeInTheDocument();
    });

    it('should clear the filtration when category is selected two times', () => {
        const rendered = render(<MainPage />);

        const categoryBadge = rendered.getAllByText('Одежда')[0];
        fireEvent.click(categoryBadge);
        fireEvent.click(categoryBadge);

        expect(rendered.getByText('Костюм гуся')).toBeInTheDocument();
        expect(rendered.getByText('Принтер')).toBeInTheDocument();
    })
});
