import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Categories } from './Categories';

afterEach(jest.clearAllMocks);

describe('Categories test', () => {
    it('should render correctly', () => {
        const rendered = render(<Categories selectedCategories={[]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for selected badge', () => {
        const rendered = render(<Categories selectedCategories={['Одежда']} />);

        expect(rendered.getByText('Одежда')).toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
            'categories__badge_selected'
        );
    });

    it('should add class for selected badges', () => {
        const rendered = render(<Categories selectedCategories={['Одежда', 'Электроника']} />);

        expect(rendered.getByText('Одежда')).toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
          'categories__badge_selected'
        );
    });

    it('should add class for selected badge (zero)', () => {
        const rendered = render(<Categories selectedCategories={[]} />);

        expect(rendered.getByText('Одежда')).not.toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
          'categories__badge_selected'
        );
    });

    it('should add class for selected badge (none selected)', () => {
        const rendered = render(<Categories selectedCategories={[]} />);

        expect(rendered.getByText('Одежда')).not.toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
          'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
          'categories__badge_selected'
        );
    });

    it('should call callback when category click', () => {
        const onCategoryClick = jest.fn();
        const rendered = render(
            <Categories
                selectedCategories={[]}
                onCategoryClick={onCategoryClick}
            />
        );

        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
        fireEvent.click(rendered.getByText('Электроника'));
        expect(onCategoryClick).toHaveBeenCalledTimes(2);
    });
});
