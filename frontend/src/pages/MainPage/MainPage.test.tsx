import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime } from '../../hooks/useCurrentTime';

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(() => new Date(2004, 9, 12, 20).toLocaleTimeString('ru-RU')),
  }));

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(useCurrentTime()).toBe("20:00:00");
        expect(rendered.asFragment()).toMatchSnapshot();
    }); 

    it('should have all and image ', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('VK Маркет')).toHaveClass(
            'main-page__title'
        );

    });

    it('should add 1 to count', () => {
        const rendered = render(<MainPage />)
        const category = rendered.getAllByText('Одежда')

        fireEvent.click(category[0])
        expect(category[0]).toHaveClass('categories__badge_selected')
    })
});
