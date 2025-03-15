import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from '../MainPage';
import { useProducts, useCurrentTime } from '../../../hooks';

jest.mock('../../../hooks', () => ({
    useProducts: jest.fn(),
    useCurrentTime: jest.fn(),
}));

describe('MainPage test', () => {
    const mockProducts = [
        {
            id: 1,
            name: 'Product 1',
            description: 'Description 1',
            price: 100,
            category: 'Электроника',
        },
        {
            id: 2,
            name: 'Product 2',
            description: 'Description 2',
            price: 200,
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Product 3',
            description: 'Description 3',
            price: 300,
            category: 'Для дома',
        },
    ];

    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(mockProducts);
        (useCurrentTime as jest.Mock).mockReturnValue('12:00:00');
    });

    it('should match the snapshot', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render the current time', () => {
        render(<MainPage />);
        expect(screen.getByText('12:00:00')).toBeInTheDocument();
    });

    it('should render the categories', () => {
        render(<MainPage />);
        expect(
            screen.getByText('Одежда', { selector: '.categories__badge' })
        ).toBeInTheDocument();
        expect(
            screen.getByText('Для дома', { selector: '.categories__badge' })
        ).toBeInTheDocument();
        expect(
            screen.getByText('Электроника', { selector: '.categories__badge' })
        ).toBeInTheDocument();
    });

    it('should render all products when no category is selected', () => {
        render(<MainPage />);

        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
    });

    it('should filter products when a category is selected', () => {
        render(<MainPage />);

        fireEvent.click(
            screen.getByText('Электроника', { selector: '.categories__badge' })
        );

        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.queryByText('Product 2')).not.toBeInTheDocument();
        expect(screen.queryByText('Product 3')).not.toBeInTheDocument();
    });

    it('should clear the filter when the same category is clicked again', () => {
        render(<MainPage />);

        fireEvent.click(
            screen.getByText('Электроника', { selector: '.categories__badge' })
        );

        fireEvent.click(
            screen.getByText('Электроника', { selector: '.categories__badge' })
        );

        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
    });
});
