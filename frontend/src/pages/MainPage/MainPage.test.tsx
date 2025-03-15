import React from 'react';
import '@testing-library/jest-dom';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';

beforeEach(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2025-03-15T01:00:00'));
});

afterEach(jest.useRealTimers);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
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
