import React from 'react';
import * as currentTimeHook from '../../hooks/useCurrentTime';
import * as productsHook from '../../hooks/useProducts';
import { Category, Product } from '../../types';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';

describe('test main page component', () => {
    beforeAll(() => {
        
        jest.spyOn(currentTimeHook, 'useCurrentTime').mockReturnValue(
            '00:00:00'
        );

        jest.mock('../../../components/Categories', () => ({
            Categories: ({
                selectedCategories,
                onCategoryClick,
            }: {
                selectedCategories: Category[];
                onCategoryClick?: (category: Category) => void;
            }) => (
                <div data-testid="categories">
                    {['Электроника', 'Одежда', 'Для дома'].map((category) => (
                        <button
                            key={category}
                            onClick={() => onCategoryClick?.(category as Category)}
                            data-testid={`category-${category}`}
                        >
                            {category}
                        </button>
                    ))}
                </div>
            ),
        }));
        
        jest.spyOn(productsHook, 'useProducts').mockReturnValue([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
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
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ] as Product[]);
    });

    afterEach(() => {
        jest.resetAllMocks();
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.getByText('Принтер'));
    });
});