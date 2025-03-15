import { fireEvent, render } from '@testing-library/react';
import { MainPage } from './MainPage';
import '@testing-library/jest-dom';
import React from 'react';
import { act } from 'react-dom/test-utils';
import { Category } from '../../types';

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('should render correctly', () => {
        const mockDate = new Date(2025, 3, 13, 20, 0, 0);
        jest.spyOn(global, 'Date').mockImplementationOnce(() => mockDate);

        const rendered = render(<MainPage></MainPage>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    const categories = ['Одежда', 'Для дома', 'Электроника'];
    const products = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    jest.mock('../../hooks', () => ({
        useProducts: () => products,
    }));

    it('should render all categories by default', () => {
        const rendered = render(<MainPage />);
        products.forEach((product) => {
            expect(rendered.getByText(product.name)).toBeInTheDocument();
        });
    });

    it('should render selected categories', () => {
        categories.forEach((category) => {
            const rendered = render(<MainPage></MainPage>);
            const categoryBadge = rendered.getByText(category, {
                selector: '.categories__badge',
            });
            fireEvent.click(categoryBadge);
            products.forEach((product) => {
                if (product.category === category) {
                    expect(
                        rendered.getByText(product.name)
                    ).toBeInTheDocument();
                } else {
                    expect(
                        rendered.queryByText(product.name)
                    ).not.toBeInTheDocument();
                }
            });
            rendered.unmount();
        });
    });

    it('should render several selected categories', () => {
        const rendered = render(<MainPage />);
        const selectedCategories: string[] = [];
        categories.forEach((category) => {
            const categoryBadge = rendered.getByText(category, {
                selector: '.categories__badge',
            });
            fireEvent.click(categoryBadge);
            selectedCategories.push(category);
            products.forEach((product) => {
                if (selectedCategories.includes(product.category)) {
                    expect(
                        rendered.queryByText(product.name)
                    ).toBeInTheDocument();
                } else {
                    expect(
                        rendered.queryByText(product.name)
                    ).not.toBeInTheDocument();
                }
            });
        });
    });
});

describe('MainPage time test', () => {
    beforeEach(() => {
        jest.useFakeTimers();
    });

    afterEach(() => {
        jest.restoreAllMocks();
        jest.useRealTimers();
    });

    it('has correct current initial time', () => {
        const mockDate = new Date(2025, 3, 13, 20, 0, 0);
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);

        const rendered = render(<MainPage></MainPage>);
        expect(
            rendered.getByText(mockDate.toLocaleTimeString('ru-RU'))
        ).toBeInTheDocument();
    });

    it('has correct current updated time after 5 seconds', () => {
        const mockDate = new Date(2025, 3, 13, 20, 0, 0);
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);

        const rendered = render(<MainPage></MainPage>);
        mockDate.setSeconds(mockDate.getSeconds() + 5);
        act(() => {
            jest.advanceTimersByTime(5000);
        });
        expect(
            rendered.getByText(mockDate.toLocaleTimeString('ru-RU'))
        ).toBeInTheDocument();
    });
});
