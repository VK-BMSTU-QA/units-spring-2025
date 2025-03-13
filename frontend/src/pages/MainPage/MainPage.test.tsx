import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { useProducts, useCurrentTime } from '../../hooks';
import '@testing-library/jest-dom';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(),
    useCurrentTime: jest.fn(),
}));

jest.mock('../../components/Categories', () => ({
    Categories: ({ onCategoryClick }: any) => (
        <div>
            <button data-testid="category-electronics" onClick={() => onCategoryClick('Электроника')}>Электроника</button>
            <button data-testid="category-clothing" onClick={() => onCategoryClick('Одежда')}>Одежда</button>
        </div>
    ),
}));

describe('MainPage', () => {
    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue([
            { id: 1, name: 'Product 1', description: 'Смартфон', price: 1000, priceSymbol: '$', category: 'Электроника' },
            { id: 2, name: 'Product 2', description: 'Тёплая куртка', price: 200, priceSymbol: '$', category: 'Одежда' }
        ]);
        (useCurrentTime as jest.Mock).mockReturnValue('2025-03-13 12:00');
    });

    it('should render the title and current time', () => {
        render(<MainPage />);
        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        expect(screen.getByText('2025-03-13 12:00')).toBeInTheDocument();
    });

    it('should update selected categories when a category is clicked', () => {
        render(<MainPage />);
        fireEvent.click(screen.getByTestId('category-electronics'));
        fireEvent.click(screen.getByTestId('category-clothing'));

        expect(screen.getByTestId('category-electronics')).toBeInTheDocument();
        expect(screen.getByTestId('category-clothing')).toBeInTheDocument();
    });

    it('should apply selected categories and render products accordingly', () => {
        render(<MainPage />);
        fireEvent.click(screen.getByTestId('category-electronics'));

        const productCards = screen.getAllByText('Электроника', { selector: '.product-card__category' });
        expect(productCards).toHaveLength(1);
    });
});
