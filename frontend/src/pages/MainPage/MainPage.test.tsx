import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);

describe('Categories test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    }); 

    it('should have all and image ', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('VK Маркет')).toHaveClass(
            'main-page__title'
        );
        expect(rendered.getByText('description')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('1 $')).toHaveClass(
            'product-card__price'
        );
        expect(rendered.getByText('Для дома')).toHaveClass(
            'product-card__category'
        );
        expect(rendered.getByAltText('name')).toHaveClass(
            'product-card__image'
        );

    });
});
