import { render, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import '@testing-library/jest-dom';
import { Product } from '../../types';
import { useProducts } from '../../hooks';

jest.mock('../../hooks', () => {
    const originalModule = jest.requireActual('../../hooks');
    return {
        ...originalModule,
        useCurrentTime: jest.fn(() => '00:00:00'),
    };
});

jest.mock('../../components', () => {
    const actual = jest.requireActual('../../components');
    return {
        ...actual,
        Categories: ({
            onCategoryClick,
        }: {
            onCategoryClick: (cat: string) => void;
        }) => {
            return (
                <div data-testid="mocked-categories">
                    <span
                        data-testid="electronics-badge"
                        className="categories__badge"
                        onClick={() => onCategoryClick('Электроника')}
                    >
                        Электроника
                    </span>
                </div>
            );
        },
    };
});

afterEach(jest.clearAllMocks);

describe('test MainPage', () => {
    it('should return render snapshot', () => {
        const mainPage = render(<MainPage />);
        expect(mainPage.asFragment()).toMatchSnapshot();
    });

    it('should display time from mock', () => {
        const mainPage = render(<MainPage />);
        expect(mainPage.getByText('00:00:00')).toBeInTheDocument();
    });

    it('should return filtered products if categories selected', () => {
        const mainPage = render(<MainPage />);
        const products: Product[] = useProducts();
        const electronicsBadge = mainPage.getByTestId('electronics-badge');
        expect(electronicsBadge).toBeInTheDocument();
        fireEvent.click(electronicsBadge);
        products.forEach((product) => {
            if (product.category === 'Электроника') {
                expect(mainPage.getByText(product.name)).toBeInTheDocument();
            }
        });
    });
});
