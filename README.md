# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.35</td>
    <td align="right">6.35</td>
    <td align="right">4.27</td>
    <td align="right">7.38</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.01</td>
    <td align="right">12.04</td>
    <td align="right">18.12</td>
    <td align="right">19.31</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.76</td>
    <td align="right">5.10</td>
    <td align="right">5.10</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.59</td>
    <td align="right">17.96</td>
    <td align="right">19.28</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.00</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.35</td>
    <td align="right">21.55</td>
    <td align="right">18.14</td>
    <td align="right">22.14</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.63</td>
    <td align="right">5.64</td>
    <td align="right">5.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">6.03</td>
    <td align="right">6.04</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.23</td>
    <td align="right">27.69</td>
    <td align="right">18.55</td>
    <td align="right">23.18</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.99</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.83</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.48</td>
    <td align="right">6.95</td>
    <td align="right">6.95</td>
    <td align="right">6.97</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">2.97</td>
    <td align="right">2.96</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">9.26</td>
    <td align="right">9.26</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.66</td>
    <td align="right">9.66</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.19</td>
    <td align="right">11.79</td>
    <td align="right">11.80</td>
    <td align="right">11.79</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">13.71</td>
    <td align="right">13.70</td>
    <td align="right">13.72</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.79</td>
    <td align="right">5.85</td>
    <td align="right">4.17</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.41</td>
    <td align="right">12.74</td>
    <td align="right">12.72</td>
    <td align="right">12.75</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.63</td>
    <td align="right">15.10</td>
    <td align="right">15.10</td>
    <td align="right">15.13</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.84</td>
    <td align="right">5.91</td>
    <td align="right">4.19</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.17</td>
    <td align="right">2.78</td>
    <td align="right">2.78</td>
    <td align="right">2.79</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.60</td>
    <td align="right">4.78</td>
    <td align="right">4.79</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.79</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.33</td>
    <td align="right">2.85</td>
    <td align="right">2.86</td>
    <td align="right">2.85</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.82</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.58</td>
    <td align="right">5.67</td>
    <td align="right">3.91</td>
    <td align="right">6.33</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.53</td>
    <td align="right">8.21</td>
    <td align="right">6.18</td>
    <td align="right">8.74</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.77</td>
    <td align="right">8.01</td>
    <td align="right">6.18</td>
    <td align="right">8.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.60</td>
    <td align="right">5.70</td>
    <td align="right">3.92</td>
    <td align="right">6.40</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.42</td>
    <td align="right">9.41</td>
    <td align="right">6.27</td>
    <td align="right">8.97</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.66</td>
    <td align="right">9.22</td>
    <td align="right">6.25</td>
    <td align="right">8.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.42</td>
    <td align="right">7.34</td>
    <td align="right">14.51</td>
    <td align="right">15.85</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.79</td>
    <td align="right">18.88</td>
    <td align="right">19.37</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.27</td>
    <td align="right">11.18</td>
    <td align="right">11.19</td>
    <td align="right">11.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.40</td>
    <td align="right">14.41</td>
    <td align="right">16.81</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.55</td>
    <td align="right">10.52</td>
    <td align="right">16.16</td>
    <td align="right">18.44</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.01</td>
    <td align="right">14.33</td>
    <td align="right">14.36</td>
    <td align="right">14.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.93</td>
    <td align="right">14.06</td>
    <td align="right">16.85</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.98</td>
    <td align="right">12.95</td>
    <td align="right">17.33</td>
    <td align="right">20.16</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.47</td>
    <td align="right">16.34</td>
    <td align="right">16.29</td>
    <td align="right">16.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.86</td>
    <td align="right">14.36</td>
    <td align="right">14.76</td>
    <td align="right">17.91</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.62</td>
    <td align="right">15.17</td>
    <td align="right">16.93</td>
    <td align="right">19.47</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.72</td>
    <td align="right">21.12</td>
    <td align="right">20.96</td>
    <td align="right">21.09</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">57.87</td>
    <td align="right">22.89</td>
    <td align="right">14.77</td>
    <td align="right">21.66</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">16.33</td>
    <td align="right">18.22</td>
    <td align="right">21.32</td>
    <td align="right">23.02</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.10</td>
    <td align="right">5.77</td>
    <td align="right">5.78</td>
    <td align="right">5.78</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.18</td>
    <td align="right">6.90</td>
    <td align="right">6.90</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">50.52</td>
    <td align="right">55.24</td>
    <td align="right">28.32</td>
    <td align="right">32.78</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.68</td>
    <td align="right">12.58</td>
    <td align="right">12.54</td>
    <td align="right">12.52</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.57</td>
    <td align="right">12.62</td>
    <td align="right">12.63</td>
    <td align="right">12.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.58</td>
    <td align="right">94.46</td>
    <td align="right">33.88</td>
    <td align="right">43.02</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.89</td>
    <td align="right">18.71</td>
    <td align="right">18.69</td>
    <td align="right">18.69</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.14</td>
    <td align="right">19.34</td>
    <td align="right">19.34</td>
    <td align="right">19.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.34</td>
    <td align="right">136.99</td>
    <td align="right">40.08</td>
    <td align="right">54.51</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.37</td>
    <td align="right">22.45</td>
    <td align="right">22.46</td>
    <td align="right">22.44</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">23.08</td>
    <td align="right">25.73</td>
    <td align="right">25.74</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">7.12</td>
    <td align="right">8.02</td>
    <td align="right">7.88</td>
    <td align="right">7.88</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.70</td>
    <td align="right">9.44</td>
    <td align="right">9.43</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.21</td>
    <td align="right">3.98</td>
    <td align="right">3.96</td>
    <td align="right">3.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.64</td>
    <td align="right">17.20</td>
    <td align="right">17.15</td>
    <td align="right">17.18</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.82</td>
    <td align="right">21.22</td>
    <td align="right">21.17</td>
    <td align="right">21.19</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.83</td>
    <td align="right">8.30</td>
    <td align="right">8.11</td>
    <td align="right">8.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.78</td>
    <td align="right">31.41</td>
    <td align="right">31.41</td>
    <td align="right">31.41</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.60</td>
    <td align="right">35.35</td>
    <td align="right">35.35</td>
    <td align="right">35.45</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.37</td>
    <td align="right">21.06</td>
    <td align="right">15.13</td>
    <td align="right">16.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.38</td>
    <td align="right">39.54</td>
    <td align="right">39.53</td>
    <td align="right">39.53</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.93</td>
    <td align="right">51.38</td>
    <td align="right">51.38</td>
    <td align="right">51.34</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.87</td>
    <td align="right">24.17</td>
    <td align="right">16.86</td>
    <td align="right">18.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.19</td>
    <td align="right">3.85</td>
    <td align="right">3.88</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.81</td>
    <td align="right">6.06</td>
    <td align="right">6.05</td>
    <td align="right">6.03</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.44</td>
    <td align="right">6.55</td>
    <td align="right">6.52</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.83</td>
    <td align="right">8.70</td>
    <td align="right">8.73</td>
    <td align="right">8.70</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.79</td>
    <td align="right">10.88</td>
    <td align="right">10.85</td>
    <td align="right">10.86</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.56</td>
    <td align="right">12.84</td>
    <td align="right">12.86</td>
    <td align="right">12.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">19.32</td>
    <td align="right">21.31</td>
    <td align="right">15.14</td>
    <td align="right">16.75</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.41</td>
    <td align="right">27.02</td>
    <td align="right">22.17</td>
    <td align="right">23.49</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.91</td>
    <td align="right">26.99</td>
    <td align="right">22.16</td>
    <td align="right">23.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.76</td>
    <td align="right">24.36</td>
    <td align="right">16.79</td>
    <td align="right">18.54</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.04</td>
    <td align="right">37.44</td>
    <td align="right">25.28</td>
    <td align="right">26.92</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">30.34</td>
    <td align="right">37.41</td>
    <td align="right">25.35</td>
    <td align="right">26.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.09</td>
    <td align="right">9.03</td>
    <td align="right">15.97</td>
    <td align="right">17.62</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.92</td>
    <td align="right">10.66</td>
    <td align="right">20.65</td>
    <td align="right">21.69</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.82</td>
    <td align="right">15.01</td>
    <td align="right">15.04</td>
    <td align="right">15.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.81</td>
    <td align="right">18.02</td>
    <td align="right">18.67</td>
    <td align="right">21.80</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.71</td>
    <td align="right">21.77</td>
    <td align="right">21.11</td>
    <td align="right">24.03</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.55</td>
    <td align="right">30.95</td>
    <td align="right">30.98</td>
    <td align="right">30.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.82</td>
    <td align="right">29.38</td>
    <td align="right">22.47</td>
    <td align="right">27.04</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.83</td>
    <td align="right">34.49</td>
    <td align="right">26.70</td>
    <td align="right">32.06</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.61</td>
    <td align="right">50.60</td>
    <td align="right">50.62</td>
    <td align="right">50.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.74</td>
    <td align="right">43.71</td>
    <td align="right">25.29</td>
    <td align="right">32.10</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.39</td>
    <td align="right">52.36</td>
    <td align="right">29.30</td>
    <td align="right">35.06</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.89</td>
    <td align="right">75.07</td>
    <td align="right">75.27</td>
    <td align="right">75.24</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.91</td>
    <td align="right">5.42</td>
    <td align="right">4.20</td>
    <td align="right">6.96</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.33</td>
    <td align="right">10.88</td>
    <td align="right">17.44</td>
    <td align="right">18.78</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.04</td>
    <td align="right">4.07</td>
    <td align="right">4.06</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.05</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.58</td>
    <td align="right">15.99</td>
    <td align="right">18.46</td>
    <td align="right">21.26</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.55</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.05</td>
    <td align="right">19.99</td>
    <td align="right">17.59</td>
    <td align="right">21.29</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.98</td>
    <td align="right">5.28</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.91</td>
    <td align="right">5.73</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.76</td>
    <td align="right">24.07</td>
    <td align="right">18.24</td>
    <td align="right">22.64</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.25</td>
    <td align="right">3.89</td>
    <td align="right">3.90</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.31</td>
    <td align="right">3.72</td>
    <td align="right">3.70</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">2.67</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.35</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.10</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.86</td>
    <td align="right">7.74</td>
    <td align="right">7.72</td>
    <td align="right">7.72</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.03</td>
    <td align="right">7.50</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.43</td>
    <td align="right">4.48</td>
    <td align="right">3.35</td>
    <td align="right">5.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.24</td>
    <td align="right">8.28</td>
    <td align="right">8.29</td>
    <td align="right">8.28</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.00</td>
    <td align="right">8.40</td>
    <td align="right">8.39</td>
    <td align="right">8.40</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.46</td>
    <td align="right">4.51</td>
    <td align="right">3.34</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.87</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.92</td>
    <td align="right">4.20</td>
    <td align="right">4.19</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.07</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.96</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.48</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.27</td>
    <td align="right">4.13</td>
    <td align="right">4.12</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.49</td>
    <td align="right">4.23</td>
    <td align="right">3.18</td>
    <td align="right">5.68</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.87</td>
    <td align="right">6.30</td>
    <td align="right">5.18</td>
    <td align="right">7.65</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.05</td>
    <td align="right">6.15</td>
    <td align="right">4.95</td>
    <td align="right">7.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.25</td>
    <td align="right">3.15</td>
    <td align="right">5.71</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.99</td>
    <td align="right">7.30</td>
    <td align="right">5.24</td>
    <td align="right">7.93</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.29</td>
    <td align="right">7.05</td>
    <td align="right">5.05</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.32</td>
    <td align="right">6.64</td>
    <td align="right">13.71</td>
    <td align="right">15.68</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">7.89</td>
    <td align="right">18.13</td>
    <td align="right">18.91</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.35</td>
    <td align="right">10.24</td>
    <td align="right">10.51</td>
    <td align="right">10.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.61</td>
    <td align="right">9.06</td>
    <td align="right">13.43</td>
    <td align="right">15.61</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.56</td>
    <td align="right">9.29</td>
    <td align="right">15.36</td>
    <td align="right">17.63</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.72</td>
    <td align="right">14.48</td>
    <td align="right">14.49</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.97</td>
    <td align="right">10.65</td>
    <td align="right">13.22</td>
    <td align="right">15.55</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.53</td>
    <td align="right">12.04</td>
    <td align="right">16.38</td>
    <td align="right">19.07</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.64</td>
    <td align="right">15.81</td>
    <td align="right">15.79</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.40</td>
    <td align="right">14.06</td>
    <td align="right">17.01</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.18</td>
    <td align="right">13.65</td>
    <td align="right">15.79</td>
    <td align="right">18.78</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.86</td>
    <td align="right">20.70</td>
    <td align="right">20.95</td>
    <td align="right">20.92</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.05</td>
    <td align="right">23.10</td>
    <td align="right">14.68</td>
    <td align="right">21.30</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">16.16</td>
    <td align="right">16.72</td>
    <td align="right">20.56</td>
    <td align="right">22.25</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.41</td>
    <td align="right">5.44</td>
    <td align="right">5.45</td>
    <td align="right">5.46</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.05</td>
    <td align="right">6.72</td>
    <td align="right">6.66</td>
    <td align="right">6.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.68</td>
    <td align="right">49.32</td>
    <td align="right">26.28</td>
    <td align="right">30.98</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.53</td>
    <td align="right">11.52</td>
    <td align="right">11.48</td>
    <td align="right">11.52</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.29</td>
    <td align="right">12.34</td>
    <td align="right">12.38</td>
    <td align="right">12.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.90</td>
    <td align="right">86.56</td>
    <td align="right">31.62</td>
    <td align="right">40.01</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.44</td>
    <td align="right">18.53</td>
    <td align="right">18.54</td>
    <td align="right">18.54</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.33</td>
    <td align="right">19.30</td>
    <td align="right">19.34</td>
    <td align="right">19.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.12</td>
    <td align="right">120.05</td>
    <td align="right">36.97</td>
    <td align="right">49.84</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.31</td>
    <td align="right">22.18</td>
    <td align="right">22.19</td>
    <td align="right">22.28</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.12</td>
    <td align="right">15.42</td>
    <td align="right">15.42</td>
    <td align="right">15.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.42</td>
    <td align="right">5.24</td>
    <td align="right">5.25</td>
    <td align="right">5.25</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.61</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.19</td>
    <td align="right">4.14</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.19</td>
    <td align="right">11.02</td>
    <td align="right">11.09</td>
    <td align="right">11.05</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.05</td>
    <td align="right">11.50</td>
    <td align="right">11.54</td>
    <td align="right">11.56</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.67</td>
    <td align="right">7.40</td>
    <td align="right">7.37</td>
    <td align="right">7.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">18.50</td>
    <td align="right">22.58</td>
    <td align="right">22.58</td>
    <td align="right">22.57</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.79</td>
    <td align="right">22.59</td>
    <td align="right">22.56</td>
    <td align="right">22.55</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.26</td>
    <td align="right">16.64</td>
    <td align="right">12.60</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.00</td>
    <td align="right">29.73</td>
    <td align="right">29.77</td>
    <td align="right">29.76</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">23.99</td>
    <td align="right">30.99</td>
    <td align="right">30.97</td>
    <td align="right">31.00</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.02</td>
    <td align="right">18.66</td>
    <td align="right">14.09</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.97</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.07</td>
    <td align="right">5.56</td>
    <td align="right">5.59</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.81</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.48</td>
    <td align="right">7.48</td>
    <td align="right">7.48</td>
    <td align="right">7.48</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.54</td>
    <td align="right">10.21</td>
    <td align="right">10.28</td>
    <td align="right">10.21</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.97</td>
    <td align="right">11.29</td>
    <td align="right">11.30</td>
    <td align="right">11.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.51</td>
    <td align="right">16.52</td>
    <td align="right">12.12</td>
    <td align="right">13.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.22</td>
    <td align="right">21.46</td>
    <td align="right">17.00</td>
    <td align="right">18.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.05</td>
    <td align="right">21.30</td>
    <td align="right">16.84</td>
    <td align="right">18.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.13</td>
    <td align="right">18.51</td>
    <td align="right">13.51</td>
    <td align="right">15.32</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.21</td>
    <td align="right">29.52</td>
    <td align="right">18.97</td>
    <td align="right">21.20</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">24.49</td>
    <td align="right">26.85</td>
    <td align="right">18.93</td>
    <td align="right">20.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.16</td>
    <td align="right">8.44</td>
    <td align="right">15.41</td>
    <td align="right">17.39</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.36</td>
    <td align="right">9.45</td>
    <td align="right">19.57</td>
    <td align="right">20.78</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">12.80</td>
    <td align="right">12.61</td>
    <td align="right">12.62</td>
    <td align="right">12.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.50</td>
    <td align="right">17.03</td>
    <td align="right">18.56</td>
    <td align="right">21.13</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.58</td>
    <td align="right">19.81</td>
    <td align="right">19.88</td>
    <td align="right">22.74</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.28</td>
    <td align="right">32.95</td>
    <td align="right">32.98</td>
    <td align="right">32.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.75</td>
    <td align="right">27.57</td>
    <td align="right">21.84</td>
    <td align="right">25.67</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">37.26</td>
    <td align="right">33.91</td>
    <td align="right">25.08</td>
    <td align="right">29.77</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.92</td>
    <td align="right">49.30</td>
    <td align="right">49.22</td>
    <td align="right">49.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">44.14</td>
    <td align="right">36.63</td>
    <td align="right">24.53</td>
    <td align="right">30.77</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">53.87</td>
    <td align="right">41.37</td>
    <td align="right">26.43</td>
    <td align="right">32.73</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.22</td>
    <td align="right">71.47</td>
    <td align="right">70.72</td>
    <td align="right">70.77</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.67</td>
    <td align="right">2.56</td>
    <td align="right">1.96</td>
    <td align="right">4.48</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">4.17</td>
    <td align="right">11.43</td>
    <td align="right">11.78</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.31</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.63</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.44</td>
    <td align="right">6.08</td>
    <td align="right">12.01</td>
    <td align="right">12.82</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.68</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.57</td>
    <td align="right">7.32</td>
    <td align="right">11.24</td>
    <td align="right">12.78</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.89</td>
    <td align="right">9.28</td>
    <td align="right">11.36</td>
    <td align="right">13.37</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.28</td>
    <td align="right">1.75</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.29</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.99</td>
    <td align="right">1.68</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.82</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
    <td align="right">2.15</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.07</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.03</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.92</td>
    <td align="right">2.41</td>
    <td align="right">1.76</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.64</td>
    <td align="right">3.35</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.78</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="right">3.57</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">1.73</td>
    <td align="right">3.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.30</td>
    <td align="right">1.75</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.29</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.58</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.86</td>
    <td align="right">1.87</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.80</td>
    <td align="right">2.15</td>
    <td align="right">2.17</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.89</td>
    <td align="right">2.39</td>
    <td align="right">1.76</td>
    <td align="right">3.88</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">2.90</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.12</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="right">3.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.96</td>
    <td align="right">2.86</td>
    <td align="right">1.71</td>
    <td align="right">3.83</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.63</td>
    <td align="right">3.35</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">3.59</td>
    <td align="right">3.57</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.23</td>
    <td align="right">3.27</td>
    <td align="right">10.22</td>
    <td align="right">10.90</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">7.00</td>
    <td align="right">3.93</td>
    <td align="right">12.71</td>
    <td align="right">12.90</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.69</td>
    <td align="right">4.86</td>
    <td align="right">4.87</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="right">9.99</td>
    <td align="right">11.10</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.46</td>
    <td align="right">4.53</td>
    <td align="right">10.49</td>
    <td align="right">12.03</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.85</td>
    <td align="right">6.77</td>
    <td align="right">6.78</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.49</td>
    <td align="right">5.24</td>
    <td align="right">9.74</td>
    <td align="right">11.00</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.51</td>
    <td align="right">5.75</td>
    <td align="right">11.28</td>
    <td align="right">13.01</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.05</td>
    <td align="right">7.55</td>
    <td align="right">7.54</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.00</td>
    <td align="right">6.35</td>
    <td align="right">10.27</td>
    <td align="right">11.64</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">6.39</td>
    <td align="right">10.71</td>
    <td align="right">12.72</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.21</td>
    <td align="right">10.66</td>
    <td align="right">10.64</td>
    <td align="right">10.66</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.12</td>
    <td align="right">11.31</td>
    <td align="right">6.12</td>
    <td align="right">9.58</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.73</td>
    <td align="right">6.17</td>
    <td align="right">12.99</td>
    <td align="right">13.53</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.07</td>
    <td align="right">2.02</td>
    <td align="right">2.02</td>
    <td align="right">2.03</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.14</td>
    <td align="right">2.05</td>
    <td align="right">2.06</td>
    <td align="right">2.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.48</td>
    <td align="right">11.52</td>
    <td align="right">16.13</td>
    <td align="right">18.18</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.58</td>
    <td align="right">3.57</td>
    <td align="right">3.50</td>
    <td align="right">3.54</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.30</td>
    <td align="right">3.46</td>
    <td align="right">3.21</td>
    <td align="right">3.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">30.65</td>
    <td align="right">25.06</td>
    <td align="right">18.55</td>
    <td align="right">22.17</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.07</td>
    <td align="right">6.53</td>
    <td align="right">6.37</td>
    <td align="right">6.26</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.71</td>
    <td align="right">6.19</td>
    <td align="right">6.50</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.01</td>
    <td align="right">38.93</td>
    <td align="right">20.72</td>
    <td align="right">27.46</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.22</td>
    <td align="right">7.92</td>
    <td align="right">7.82</td>
    <td align="right">8.04</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.94</td>
    <td align="right">6.37</td>
    <td align="right">6.45</td>
    <td align="right">6.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.73</td>
    <td align="right">2.60</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.75</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
    <td align="right">2.62</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.42</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.94</td>
    <td align="right">4.12</td>
    <td align="right">4.07</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.19</td>
    <td align="right">4.63</td>
    <td align="right">4.60</td>
    <td align="right">4.53</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.72</td>
    <td align="right">3.34</td>
    <td align="right">3.43</td>
    <td align="right">3.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">11.08</td>
    <td align="right">10.05</td>
    <td align="right">9.88</td>
    <td align="right">9.90</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.92</td>
    <td align="right">9.66</td>
    <td align="right">9.21</td>
    <td align="right">9.64</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.54</td>
    <td align="right">7.51</td>
    <td align="right">5.34</td>
    <td align="right">7.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">16.06</td>
    <td align="right">13.01</td>
    <td align="right">12.84</td>
    <td align="right">12.98</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.88</td>
    <td align="right">13.55</td>
    <td align="right">13.80</td>
    <td align="right">14.08</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.21</td>
    <td align="right">11.22</td>
    <td align="right">6.87</td>
    <td align="right">7.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.39</td>
    <td align="right">2.55</td>
    <td align="right">2.56</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.73</td>
    <td align="right">2.57</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.74</td>
    <td align="right">2.63</td>
    <td align="right">2.65</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">3.12</td>
    <td align="right">3.18</td>
    <td align="right">3.21</td>
    <td align="right">3.04</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.40</td>
    <td align="right">4.43</td>
    <td align="right">5.12</td>
    <td align="right">4.20</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.34</td>
    <td align="right">5.00</td>
    <td align="right">5.02</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.65</td>
    <td align="right">7.53</td>
    <td align="right">5.13</td>
    <td align="right">6.41</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.46</td>
    <td align="right">9.81</td>
    <td align="right">9.83</td>
    <td align="right">9.94</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.13</td>
    <td align="right">10.07</td>
    <td align="right">9.56</td>
    <td align="right">9.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">10.53</td>
    <td align="right">11.07</td>
    <td align="right">6.39</td>
    <td align="right">7.89</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.77</td>
    <td align="right">12.91</td>
    <td align="right">12.69</td>
    <td align="right">12.83</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.89</td>
    <td align="right">12.65</td>
    <td align="right">13.41</td>
    <td align="right">13.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.64</td>
    <td align="right">4.38</td>
    <td align="right">11.32</td>
    <td align="right">12.55</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.86</td>
    <td align="right">4.97</td>
    <td align="right">13.57</td>
    <td align="right">14.15</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.03</td>
    <td align="right">6.92</td>
    <td align="right">6.90</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.49</td>
    <td align="right">8.36</td>
    <td align="right">12.95</td>
    <td align="right">15.20</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.59</td>
    <td align="right">8.30</td>
    <td align="right">13.35</td>
    <td align="right">15.28</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.86</td>
    <td align="right">12.42</td>
    <td align="right">12.59</td>
    <td align="right">12.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">16.27</td>
    <td align="right">13.51</td>
    <td align="right">14.31</td>
    <td align="right">16.99</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">24.66</td>
    <td align="right">16.40</td>
    <td align="right">16.65</td>
    <td align="right">20.28</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">26.68</td>
    <td align="right">23.98</td>
    <td align="right">23.05</td>
    <td align="right">23.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">22.50</td>
    <td align="right">16.16</td>
    <td align="right">14.97</td>
    <td align="right">18.41</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.06</td>
    <td align="right">18.92</td>
    <td align="right">16.32</td>
    <td align="right">20.11</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.56</td>
    <td align="right">35.49</td>
    <td align="right">35.49</td>
    <td align="right">35.53</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.13</td>
    <td align="right">5.31</td>
    <td align="right">3.77</td>
    <td align="right">5.43</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.26</td>
    <td align="right">11.31</td>
    <td align="right">14.13</td>
    <td align="right">15.23</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.85</td>
    <td align="right">3.60</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.37</td>
    <td align="right">4.15</td>
    <td align="right">4.15</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.14</td>
    <td align="right">16.17</td>
    <td align="right">14.96</td>
    <td align="right">16.36</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.45</td>
    <td align="right">3.99</td>
    <td align="right">3.97</td>
    <td align="right">3.97</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.14</td>
    <td align="right">4.81</td>
    <td align="right">4.76</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.29</td>
    <td align="right">19.92</td>
    <td align="right">14.00</td>
    <td align="right">16.93</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">11.21</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">11.31</td>
    <td align="right">5.09</td>
    <td align="right">5.06</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">26.32</td>
    <td align="right">24.97</td>
    <td align="right">14.47</td>
    <td align="right">17.82</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">11.59</td>
    <td align="right">4.70</td>
    <td align="right">4.72</td>
    <td align="right">4.69</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">12.70</td>
    <td align="right">5.54</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.42</td>
    <td align="right">4.32</td>
    <td align="right">4.33</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.50</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.87</td>
    <td align="right">2.19</td>
    <td align="right">2.18</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.39</td>
    <td align="right">6.97</td>
    <td align="right">6.90</td>
    <td align="right">6.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.73</td>
    <td align="right">7.08</td>
    <td align="right">7.07</td>
    <td align="right">7.07</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.81</td>
    <td align="right">2.98</td>
    <td align="right">2.38</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">12.51</td>
    <td align="right">20.96</td>
    <td align="right">21.04</td>
    <td align="right">20.71</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">13.15</td>
    <td align="right">26.27</td>
    <td align="right">25.96</td>
    <td align="right">25.97</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">6.15</td>
    <td align="right">4.43</td>
    <td align="right">3.09</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.61</td>
    <td align="right">10.36</td>
    <td align="right">10.16</td>
    <td align="right">10.22</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">24.44</td>
    <td align="right">12.30</td>
    <td align="right">12.18</td>
    <td align="right">12.16</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.58</td>
    <td align="right">17.19</td>
    <td align="right">12.01</td>
    <td align="right">13.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.81</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.28</td>
    <td align="right">3.27</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.82</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.27</td>
    <td align="right">3.38</td>
    <td align="right">2.72</td>
    <td align="right">4.29</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.85</td>
    <td align="right">3.22</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.81</td>
    <td align="right">4.68</td>
    <td align="right">3.96</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.39</td>
    <td align="right">4.35</td>
    <td align="right">2.99</td>
    <td align="right">4.77</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.91</td>
    <td align="right">6.39</td>
    <td align="right">5.10</td>
    <td align="right">6.80</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">12.14</td>
    <td align="right">6.29</td>
    <td align="right">4.95</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.44</td>
    <td align="right">4.37</td>
    <td align="right">2.98</td>
    <td align="right">5.10</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">20.13</td>
    <td align="right">7.08</td>
    <td align="right">5.15</td>
    <td align="right">6.97</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">10.90</td>
    <td align="right">25.84</td>
    <td align="right">18.37</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.13</td>
    <td align="right">6.70</td>
    <td align="right">11.25</td>
    <td align="right">12.23</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.02</td>
    <td align="right">9.02</td>
    <td align="right">14.14</td>
    <td align="right">14.68</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.10</td>
    <td align="right">8.91</td>
    <td align="right">8.96</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.40</td>
    <td align="right">9.84</td>
    <td align="right">11.90</td>
    <td align="right">13.60</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.96</td>
    <td align="right">11.17</td>
    <td align="right">13.25</td>
    <td align="right">14.96</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.73</td>
    <td align="right">13.03</td>
    <td align="right">13.03</td>
    <td align="right">13.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.44</td>
    <td align="right">11.47</td>
    <td align="right">11.66</td>
    <td align="right">13.75</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.21</td>
    <td align="right">28.72</td>
    <td align="right">18.95</td>
    <td align="right">23.09</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">18.39</td>
    <td align="right">37.33</td>
    <td align="right">37.51</td>
    <td align="right">40.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.81</td>
    <td align="right">13.83</td>
    <td align="right">12.41</td>
    <td align="right">14.74</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">25.76</td>
    <td align="right">15.13</td>
    <td align="right">12.34</td>
    <td align="right">14.98</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">47.13</td>
    <td align="right">22.84</td>
    <td align="right">22.79</td>
    <td align="right">22.69</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.98</td>
    <td align="right">23.49</td>
    <td align="right">14.61</td>
    <td align="right">19.75</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.18</td>
    <td align="right">11.86</td>
    <td align="right">15.57</td>
    <td align="right">16.68</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.17</td>
    <td align="right">3.81</td>
    <td align="right">3.86</td>
    <td align="right">3.83</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.92</td>
    <td align="right">4.68</td>
    <td align="right">4.56</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">37.56</td>
    <td align="right">19.10</td>
    <td align="right">17.00</td>
    <td align="right">18.79</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">7.29</td>
    <td align="right">6.77</td>
    <td align="right">6.69</td>
    <td align="right">6.68</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.51</td>
    <td align="right">16.95</td>
    <td align="right">17.03</td>
    <td align="right">16.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">70.24</td>
    <td align="right">80.97</td>
    <td align="right">26.31</td>
    <td align="right">34.07</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.43</td>
    <td align="right">13.50</td>
    <td align="right">13.62</td>
    <td align="right">13.70</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">21.69</td>
    <td align="right">20.95</td>
    <td align="right">20.98</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.38</td>
    <td align="right">118.38</td>
    <td align="right">31.25</td>
    <td align="right">42.77</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">20.01</td>
    <td align="right">18.65</td>
    <td align="right">18.53</td>
    <td align="right">18.65</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">21.01</td>
    <td align="right">22.98</td>
    <td align="right">22.87</td>
    <td align="right">22.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.12</td>
    <td align="right">4.61</td>
    <td align="right">4.72</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.81</td>
    <td align="right">19.51</td>
    <td align="right">19.53</td>
    <td align="right">19.54</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.11</td>
    <td align="right">2.32</td>
    <td align="right">2.40</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.44</td>
    <td align="right">8.87</td>
    <td align="right">9.01</td>
    <td align="right">8.93</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.02</td>
    <td align="right">25.19</td>
    <td align="right">25.18</td>
    <td align="right">25.07</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.91</td>
    <td align="right">4.82</td>
    <td align="right">4.37</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">38.18</td>
    <td align="right">31.24</td>
    <td align="right">31.24</td>
    <td align="right">31.21</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">28.83</td>
    <td align="right">27.25</td>
    <td align="right">27.08</td>
    <td align="right">27.03</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.11</td>
    <td align="right">15.29</td>
    <td align="right">10.81</td>
    <td align="right">11.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.85</td>
    <td align="right">34.41</td>
    <td align="right">34.30</td>
    <td align="right">34.55</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">38.63</td>
    <td align="right">36.83</td>
    <td align="right">36.72</td>
    <td align="right">36.91</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.37</td>
    <td align="right">17.80</td>
    <td align="right">12.36</td>
    <td align="right">13.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.07</td>
    <td align="right">2.15</td>
    <td align="right">2.30</td>
    <td align="right">2.15</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.06</td>
    <td align="right">3.44</td>
    <td align="right">3.57</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.95</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.94</td>
    <td align="right">5.48</td>
    <td align="right">4.65</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.20</td>
    <td align="right">5.66</td>
    <td align="right">5.26</td>
    <td align="right">6.60</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.58</td>
    <td align="right">6.53</td>
    <td align="right">5.68</td>
    <td align="right">6.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.23</td>
    <td align="right">15.22</td>
    <td align="right">10.77</td>
    <td align="right">11.69</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.61</td>
    <td align="right">18.58</td>
    <td align="right">15.76</td>
    <td align="right">16.66</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.89</td>
    <td align="right">18.93</td>
    <td align="right">16.07</td>
    <td align="right">16.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.70</td>
    <td align="right">17.80</td>
    <td align="right">12.29</td>
    <td align="right">13.74</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">27.92</td>
    <td align="right">26.39</td>
    <td align="right">18.73</td>
    <td align="right">19.77</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.76</td>
    <td align="right">26.05</td>
    <td align="right">18.63</td>
    <td align="right">19.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.75</td>
    <td align="right">23.85</td>
    <td align="right">20.52</td>
    <td align="right">23.11</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.40</td>
    <td align="right">9.61</td>
    <td align="right">14.84</td>
    <td align="right">15.47</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.59</td>
    <td align="right">9.95</td>
    <td align="right">9.91</td>
    <td align="right">9.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.48</td>
    <td align="right">11.81</td>
    <td align="right">13.48</td>
    <td align="right">15.32</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.81</td>
    <td align="right">13.79</td>
    <td align="right">14.53</td>
    <td align="right">16.32</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">17.13</td>
    <td align="right">46.36</td>
    <td align="right">46.32</td>
    <td align="right">46.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.19</td>
    <td align="right">25.41</td>
    <td align="right">19.53</td>
    <td align="right">22.55</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.03</td>
    <td align="right">32.28</td>
    <td align="right">19.90</td>
    <td align="right">24.68</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.51</td>
    <td align="right">40.16</td>
    <td align="right">40.06</td>
    <td align="right">40.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.48</td>
    <td align="right">35.76</td>
    <td align="right">23.13</td>
    <td align="right">28.55</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.74</td>
    <td align="right">41.32</td>
    <td align="right">22.07</td>
    <td align="right">28.21</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">65.15</td>
    <td align="right">60.62</td>
    <td align="right">60.80</td>
    <td align="right">60.95</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.07</td>
    <td align="right">34.94</td>
    <td align="right">14.35</td>
    <td align="right">17.81</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.90</td>
    <td align="right">44.34</td>
    <td align="right">37.56</td>
    <td align="right">38.69</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.34</td>
    <td align="right">16.31</td>
    <td align="right">16.43</td>
    <td align="right">16.30</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.61</td>
    <td align="right">17.80</td>
    <td align="right">17.87</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.42</td>
    <td align="right">66.71</td>
    <td align="right">40.46</td>
    <td align="right">43.75</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.35</td>
    <td align="right">18.40</td>
    <td align="right">18.31</td>
    <td align="right">18.40</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.05</td>
    <td align="right">19.88</td>
    <td align="right">19.24</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.10</td>
    <td align="right">81.97</td>
    <td align="right">38.92</td>
    <td align="right">46.29</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.41</td>
    <td align="right">20.54</td>
    <td align="right">20.48</td>
    <td align="right">20.49</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.94</td>
    <td align="right">21.09</td>
    <td align="right">21.07</td>
    <td align="right">21.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.38</td>
    <td align="right">100.59</td>
    <td align="right">40.67</td>
    <td align="right">50.10</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.70</td>
    <td align="right">22.25</td>
    <td align="right">22.17</td>
    <td align="right">22.17</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.34</td>
    <td align="right">22.05</td>
    <td align="right">22.16</td>
    <td align="right">21.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.94</td>
    <td align="right">23.79</td>
    <td align="right">23.77</td>
    <td align="right">23.75</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">26.50</td>
    <td align="right">26.50</td>
    <td align="right">26.50</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.82</td>
    <td align="right">15.56</td>
    <td align="right">15.64</td>
    <td align="right">15.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.64</td>
    <td align="right">29.96</td>
    <td align="right">29.99</td>
    <td align="right">29.96</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.56</td>
    <td align="right">34.57</td>
    <td align="right">34.57</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.09</td>
    <td align="right">17.76</td>
    <td align="right">17.76</td>
    <td align="right">17.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.43</td>
    <td align="right">37.09</td>
    <td align="right">37.04</td>
    <td align="right">37.12</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.56</td>
    <td align="right">49.13</td>
    <td align="right">49.02</td>
    <td align="right">49.01</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.14</td>
    <td align="right">20.82</td>
    <td align="right">20.83</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.42</td>
    <td align="right">41.67</td>
    <td align="right">41.52</td>
    <td align="right">41.69</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.42</td>
    <td align="right">58.45</td>
    <td align="right">58.47</td>
    <td align="right">58.46</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.01</td>
    <td align="right">26.02</td>
    <td align="right">26.12</td>
    <td align="right">25.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.45</td>
    <td align="right">16.82</td>
    <td align="right">16.88</td>
    <td align="right">16.85</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.82</td>
    <td align="right">23.75</td>
    <td align="right">23.74</td>
    <td align="right">23.70</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.52</td>
    <td align="right">26.53</td>
    <td align="right">26.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">18.97</td>
    <td align="right">21.16</td>
    <td align="right">21.23</td>
    <td align="right">21.07</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.07</td>
    <td align="right">30.02</td>
    <td align="right">30.18</td>
    <td align="right">30.02</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.04</td>
    <td align="right">34.54</td>
    <td align="right">34.54</td>
    <td align="right">34.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.45</td>
    <td align="right">25.09</td>
    <td align="right">25.09</td>
    <td align="right">25.17</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.11</td>
    <td align="right">36.91</td>
    <td align="right">36.87</td>
    <td align="right">37.11</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.56</td>
    <td align="right">49.03</td>
    <td align="right">48.93</td>
    <td align="right">48.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.67</td>
    <td align="right">33.07</td>
    <td align="right">33.07</td>
    <td align="right">33.08</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.12</td>
    <td align="right">41.69</td>
    <td align="right">41.70</td>
    <td align="right">41.57</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.48</td>
    <td align="right">58.51</td>
    <td align="right">58.62</td>
    <td align="right">58.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.30</td>
    <td align="right">24.48</td>
    <td align="right">28.11</td>
    <td align="right">29.68</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.67</td>
    <td align="right">31.50</td>
    <td align="right">35.56</td>
    <td align="right">35.63</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.47</td>
    <td align="right">34.36</td>
    <td align="right">34.61</td>
    <td align="right">34.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.34</td>
    <td align="right">37.00</td>
    <td align="right">28.32</td>
    <td align="right">32.16</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.34</td>
    <td align="right">40.87</td>
    <td align="right">34.50</td>
    <td align="right">37.21</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.74</td>
    <td align="right">44.94</td>
    <td align="right">44.88</td>
    <td align="right">44.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.09</td>
    <td align="right">43.82</td>
    <td align="right">27.90</td>
    <td align="right">32.74</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.51</td>
    <td align="right">50.33</td>
    <td align="right">36.11</td>
    <td align="right">39.45</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.02</td>
    <td align="right">46.93</td>
    <td align="right">46.98</td>
    <td align="right">47.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.26</td>
    <td align="right">49.09</td>
    <td align="right">30.62</td>
    <td align="right">33.85</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.36</td>
    <td align="right">52.61</td>
    <td align="right">35.99</td>
    <td align="right">39.61</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.81</td>
    <td align="right">65.22</td>
    <td align="right">64.75</td>
    <td align="right">65.28</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">109.25</td>
    <td align="right">128.48</td>
    <td align="right">27.69</td>
    <td align="right">41.63</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">40.70</td>
    <td align="right">56.78</td>
    <td align="right">45.24</td>
    <td align="right">47.15</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.97</td>
    <td align="right">18.87</td>
    <td align="right">19.59</td>
    <td align="right">18.96</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.28</td>
    <td align="right">20.55</td>
    <td align="right">20.45</td>
    <td align="right">20.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">104.64</td>
    <td align="right">136.83</td>
    <td align="right">61.45</td>
    <td align="right">69.81</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.59</td>
    <td align="right">29.76</td>
    <td align="right">29.58</td>
    <td align="right">29.94</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.24</td>
    <td align="right">32.45</td>
    <td align="right">32.55</td>
    <td align="right">32.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">192.82</td>
    <td align="right">255.27</td>
    <td align="right">79.39</td>
    <td align="right">99.01</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.47</td>
    <td align="right">48.18</td>
    <td align="right">48.09</td>
    <td align="right">48.11</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.31</td>
    <td align="right">50.75</td>
    <td align="right">50.74</td>
    <td align="right">50.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">302.10</td>
    <td align="right">415.81</td>
    <td align="right">101.44</td>
    <td align="right">135.02</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.99</td>
    <td align="right">65.48</td>
    <td align="right">65.38</td>
    <td align="right">65.46</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">63.45</td>
    <td align="right">67.34</td>
    <td align="right">66.68</td>
    <td align="right">66.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.09</td>
    <td align="right">28.21</td>
    <td align="right">28.35</td>
    <td align="right">28.24</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.04</td>
    <td align="right">31.66</td>
    <td align="right">31.59</td>
    <td align="right">31.88</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">17.19</td>
    <td align="right">20.74</td>
    <td align="right">20.84</td>
    <td align="right">20.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.74</td>
    <td align="right">43.87</td>
    <td align="right">43.86</td>
    <td align="right">43.97</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.93</td>
    <td align="right">52.51</td>
    <td align="right">52.46</td>
    <td align="right">52.51</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">26.14</td>
    <td align="right">27.21</td>
    <td align="right">26.59</td>
    <td align="right">27.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.07</td>
    <td align="right">74.01</td>
    <td align="right">73.92</td>
    <td align="right">73.98</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">104.50</td>
    <td align="right">85.03</td>
    <td align="right">85.07</td>
    <td align="right">85.03</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">43.22</td>
    <td align="right">46.58</td>
    <td align="right">46.60</td>
    <td align="right">46.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.62</td>
    <td align="right">94.65</td>
    <td align="right">94.65</td>
    <td align="right">94.53</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.83</td>
    <td align="right">112.41</td>
    <td align="right">112.47</td>
    <td align="right">112.44</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">72.16</td>
    <td align="right">77.96</td>
    <td align="right">78.10</td>
    <td align="right">78.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.32</td>
    <td align="right">19.88</td>
    <td align="right">20.84</td>
    <td align="right">19.72</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.37</td>
    <td align="right">28.58</td>
    <td align="right">28.48</td>
    <td align="right">28.50</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.38</td>
    <td align="right">31.88</td>
    <td align="right">31.92</td>
    <td align="right">32.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.72</td>
    <td align="right">30.70</td>
    <td align="right">30.71</td>
    <td align="right">30.71</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.10</td>
    <td align="right">46.17</td>
    <td align="right">46.16</td>
    <td align="right">46.15</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.49</td>
    <td align="right">53.43</td>
    <td align="right">53.29</td>
    <td align="right">53.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">49.17</td>
    <td align="right">57.52</td>
    <td align="right">57.52</td>
    <td align="right">58.58</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.42</td>
    <td align="right">72.52</td>
    <td align="right">72.68</td>
    <td align="right">72.44</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">104.25</td>
    <td align="right">85.17</td>
    <td align="right">85.18</td>
    <td align="right">85.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">84.79</td>
    <td align="right">87.88</td>
    <td align="right">87.51</td>
    <td align="right">87.69</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.75</td>
    <td align="right">95.26</td>
    <td align="right">95.31</td>
    <td align="right">95.17</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">136.44</td>
    <td align="right">111.97</td>
    <td align="right">111.90</td>
    <td align="right">111.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.47</td>
    <td align="right">28.64</td>
    <td align="right">30.99</td>
    <td align="right">33.11</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.51</td>
    <td align="right">36.20</td>
    <td align="right">39.41</td>
    <td align="right">40.65</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">37.54</td>
    <td align="right">42.19</td>
    <td align="right">42.20</td>
    <td align="right">42.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.87</td>
    <td align="right">52.10</td>
    <td align="right">39.27</td>
    <td align="right">43.62</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.21</td>
    <td align="right">57.71</td>
    <td align="right">45.38</td>
    <td align="right">49.22</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.41</td>
    <td align="right">67.68</td>
    <td align="right">67.83</td>
    <td align="right">68.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.70</td>
    <td align="right">72.25</td>
    <td align="right">47.13</td>
    <td align="right">53.62</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.98</td>
    <td align="right">89.76</td>
    <td align="right">61.47</td>
    <td align="right">67.75</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.79</td>
    <td align="right">95.63</td>
    <td align="right">95.57</td>
    <td align="right">95.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.66</td>
    <td align="right">91.11</td>
    <td align="right">61.56</td>
    <td align="right">69.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">105.61</td>
    <td align="right">107.77</td>
    <td align="right">69.87</td>
    <td align="right">77.76</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">135.34</td>
    <td align="right">142.40</td>
    <td align="right">142.38</td>
    <td align="right">147.11</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.68</td>
    <td align="right">13.27</td>
    <td align="right">8.53</td>
    <td align="right">11.33</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.42</td>
    <td align="right">28.73</td>
    <td align="right">29.19</td>
    <td align="right">30.04</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.48</td>
    <td align="right">13.96</td>
    <td align="right">13.95</td>
    <td align="right">13.94</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.80</td>
    <td align="right">18.02</td>
    <td align="right">18.02</td>
    <td align="right">18.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.74</td>
    <td align="right">42.78</td>
    <td align="right">31.25</td>
    <td align="right">33.55</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.02</td>
    <td align="right">18.42</td>
    <td align="right">18.43</td>
    <td align="right">18.46</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">20.87</td>
    <td align="right">20.94</td>
    <td align="right">20.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.28</td>
    <td align="right">62.55</td>
    <td align="right">33.16</td>
    <td align="right">37.99</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.70</td>
    <td align="right">21.13</td>
    <td align="right">21.31</td>
    <td align="right">21.29</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">22.98</td>
    <td align="right">22.92</td>
    <td align="right">22.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.57</td>
    <td align="right">86.03</td>
    <td align="right">33.13</td>
    <td align="right">39.21</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.24</td>
    <td align="right">23.28</td>
    <td align="right">23.24</td>
    <td align="right">23.27</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.09</td>
    <td align="right">25.73</td>
    <td align="right">25.71</td>
    <td align="right">25.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.23</td>
    <td align="right">18.32</td>
    <td align="right">18.44</td>
    <td align="right">18.31</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.96</td>
    <td align="right">8.72</td>
    <td align="right">8.72</td>
    <td align="right">8.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">26.56</td>
    <td align="right">26.51</td>
    <td align="right">26.52</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">26.97</td>
    <td align="right">27.03</td>
    <td align="right">27.04</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.76</td>
    <td align="right">13.75</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.08</td>
    <td align="right">35.47</td>
    <td align="right">35.47</td>
    <td align="right">35.49</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.38</td>
    <td align="right">34.27</td>
    <td align="right">34.24</td>
    <td align="right">34.37</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.83</td>
    <td align="right">17.85</td>
    <td align="right">17.84</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.65</td>
    <td align="right">38.41</td>
    <td align="right">38.39</td>
    <td align="right">38.39</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.38</td>
    <td align="right">41.42</td>
    <td align="right">41.18</td>
    <td align="right">41.26</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.14</td>
    <td align="right">19.73</td>
    <td align="right">19.73</td>
    <td align="right">19.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.51</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">18.32</td>
    <td align="right">18.32</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">18.84</td>
    <td align="right">18.85</td>
    <td align="right">18.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.94</td>
    <td align="right">14.15</td>
    <td align="right">14.12</td>
    <td align="right">14.13</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.58</td>
    <td align="right">26.54</td>
    <td align="right">26.51</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.62</td>
    <td align="right">27.07</td>
    <td align="right">27.02</td>
    <td align="right">26.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.22</td>
    <td align="right">17.23</td>
    <td align="right">17.26</td>
    <td align="right">17.22</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.06</td>
    <td align="right">35.54</td>
    <td align="right">35.47</td>
    <td align="right">35.47</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.43</td>
    <td align="right">34.29</td>
    <td align="right">34.31</td>
    <td align="right">34.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">20.05</td>
    <td align="right">20.05</td>
    <td align="right">20.05</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.69</td>
    <td align="right">38.41</td>
    <td align="right">38.39</td>
    <td align="right">38.42</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.40</td>
    <td align="right">41.47</td>
    <td align="right">41.33</td>
    <td align="right">41.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.24</td>
    <td align="right">20.91</td>
    <td align="right">24.55</td>
    <td align="right">26.46</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.47</td>
    <td align="right">42.02</td>
    <td align="right">41.77</td>
    <td align="right">42.13</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.99</td>
    <td align="right">27.13</td>
    <td align="right">27.86</td>
    <td align="right">27.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.01</td>
    <td align="right">29.99</td>
    <td align="right">24.21</td>
    <td align="right">27.41</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.90</td>
    <td align="right">46.32</td>
    <td align="right">39.41</td>
    <td align="right">41.87</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.74</td>
    <td align="right">36.24</td>
    <td align="right">36.23</td>
    <td align="right">36.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.13</td>
    <td align="right">35.84</td>
    <td align="right">24.46</td>
    <td align="right">28.59</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.67</td>
    <td align="right">54.11</td>
    <td align="right">40.19</td>
    <td align="right">42.85</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.53</td>
    <td align="right">38.53</td>
    <td align="right">38.52</td>
    <td align="right">38.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.72</td>
    <td align="right">46.71</td>
    <td align="right">29.67</td>
    <td align="right">33.79</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">65.12</td>
    <td align="right">58.34</td>
    <td align="right">45.33</td>
    <td align="right">46.79</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.36</td>
    <td align="right">51.02</td>
    <td align="right">50.30</td>
    <td align="right">50.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">127.12</td>
    <td align="right">63.05</td>
    <td align="right">23.21</td>
    <td align="right">33.29</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.88</td>
    <td align="right">34.35</td>
    <td align="right">33.72</td>
    <td align="right">35.05</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.47</td>
    <td align="right">18.05</td>
    <td align="right">17.97</td>
    <td align="right">17.94</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.79</td>
    <td align="right">20.92</td>
    <td align="right">20.93</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">77.96</td>
    <td align="right">87.07</td>
    <td align="right">43.73</td>
    <td align="right">49.32</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.19</td>
    <td align="right">28.93</td>
    <td align="right">28.83</td>
    <td align="right">28.90</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.40</td>
    <td align="right">33.34</td>
    <td align="right">33.50</td>
    <td align="right">33.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">147.13</td>
    <td align="right">200.13</td>
    <td align="right">67.57</td>
    <td align="right">83.69</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.50</td>
    <td align="right">50.49</td>
    <td align="right">50.39</td>
    <td align="right">50.27</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">53.16</td>
    <td align="right">53.71</td>
    <td align="right">53.77</td>
    <td align="right">53.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">252.57</td>
    <td align="right">312.05</td>
    <td align="right">85.02</td>
    <td align="right">111.65</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">66.38</td>
    <td align="right">65.82</td>
    <td align="right">65.74</td>
    <td align="right">65.74</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">69.68</td>
    <td align="right">69.47</td>
    <td align="right">69.48</td>
    <td align="right">69.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.70</td>
    <td align="right">22.05</td>
    <td align="right">22.44</td>
    <td align="right">22.31</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.95</td>
    <td align="right">22.53</td>
    <td align="right">22.69</td>
    <td align="right">22.71</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.01</td>
    <td align="right">10.81</td>
    <td align="right">11.01</td>
    <td align="right">10.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.87</td>
    <td align="right">42.04</td>
    <td align="right">41.91</td>
    <td align="right">41.84</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.69</td>
    <td align="right">44.57</td>
    <td align="right">44.32</td>
    <td align="right">44.33</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.34</td>
    <td align="right">24.50</td>
    <td align="right">24.30</td>
    <td align="right">24.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.47</td>
    <td align="right">71.38</td>
    <td align="right">71.16</td>
    <td align="right">71.13</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">72.17</td>
    <td align="right">70.74</td>
    <td align="right">70.72</td>
    <td align="right">70.67</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">39.38</td>
    <td align="right">42.01</td>
    <td align="right">41.96</td>
    <td align="right">42.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.39</td>
    <td align="right">88.49</td>
    <td align="right">88.55</td>
    <td align="right">88.52</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.52</td>
    <td align="right">95.59</td>
    <td align="right">95.67</td>
    <td align="right">96.72</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">54.69</td>
    <td align="right">54.13</td>
    <td align="right">54.33</td>
    <td align="right">54.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.16</td>
    <td align="right">10.45</td>
    <td align="right">10.61</td>
    <td align="right">10.63</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.94</td>
    <td align="right">21.36</td>
    <td align="right">21.60</td>
    <td align="right">21.50</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.84</td>
    <td align="right">22.52</td>
    <td align="right">22.51</td>
    <td align="right">22.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.41</td>
    <td align="right">24.44</td>
    <td align="right">24.32</td>
    <td align="right">24.59</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.01</td>
    <td align="right">41.18</td>
    <td align="right">41.17</td>
    <td align="right">41.00</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.32</td>
    <td align="right">45.93</td>
    <td align="right">45.86</td>
    <td align="right">45.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">39.29</td>
    <td align="right">41.56</td>
    <td align="right">41.60</td>
    <td align="right">41.64</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.67</td>
    <td align="right">70.64</td>
    <td align="right">70.64</td>
    <td align="right">70.84</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.54</td>
    <td align="right">69.99</td>
    <td align="right">69.89</td>
    <td align="right">69.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">54.56</td>
    <td align="right">55.65</td>
    <td align="right">55.42</td>
    <td align="right">55.44</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.91</td>
    <td align="right">90.77</td>
    <td align="right">90.78</td>
    <td align="right">90.75</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.62</td>
    <td align="right">93.61</td>
    <td align="right">93.69</td>
    <td align="right">94.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.43</td>
    <td align="right">24.87</td>
    <td align="right">27.13</td>
    <td align="right">29.99</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.46</td>
    <td align="right">43.96</td>
    <td align="right">43.97</td>
    <td align="right">44.27</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.74</td>
    <td align="right">34.17</td>
    <td align="right">33.79</td>
    <td align="right">33.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.81</td>
    <td align="right">45.14</td>
    <td align="right">32.33</td>
    <td align="right">37.18</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">68.60</td>
    <td align="right">59.95</td>
    <td align="right">50.34</td>
    <td align="right">53.23</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.42</td>
    <td align="right">58.76</td>
    <td align="right">58.83</td>
    <td align="right">58.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">63.17</td>
    <td align="right">65.96</td>
    <td align="right">41.54</td>
    <td align="right">48.43</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.59</td>
    <td align="right">88.02</td>
    <td align="right">64.27</td>
    <td align="right">69.50</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.90</td>
    <td align="right">83.20</td>
    <td align="right">82.99</td>
    <td align="right">82.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.91</td>
    <td align="right">89.61</td>
    <td align="right">58.24</td>
    <td align="right">65.38</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.84</td>
    <td align="right">107.43</td>
    <td align="right">80.02</td>
    <td align="right">83.67</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">128.18</td>
    <td align="right">120.69</td>
    <td align="right">120.09</td>
    <td align="right">120.56</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.96</td>
    <td align="right">6.65</td>
    <td align="right">5.57</td>
    <td align="right">7.39</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">64.78</td>
    <td align="right">60.32</td>
    <td align="right">40.38</td>
    <td align="right">42.67</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.85</td>
    <td align="right">20.71</td>
    <td align="right">23.13</td>
    <td align="right">24.02</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.75</td>
    <td align="right">24.88</td>
    <td align="right">26.33</td>
    <td align="right">27.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">98.71</td>
    <td align="right">86.68</td>
    <td align="right">41.37</td>
    <td align="right">45.55</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.32</td>
    <td align="right">22.02</td>
    <td align="right">24.24</td>
    <td align="right">25.13</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.44</td>
    <td align="right">27.71</td>
    <td align="right">28.25</td>
    <td align="right">29.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">120.92</td>
    <td align="right">104.51</td>
    <td align="right">39.90</td>
    <td align="right">47.73</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.07</td>
    <td align="right">25.85</td>
    <td align="right">25.97</td>
    <td align="right">26.83</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.90</td>
    <td align="right">30.15</td>
    <td align="right">29.49</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">156.54</td>
    <td align="right">134.05</td>
    <td align="right">41.46</td>
    <td align="right">49.39</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.43</td>
    <td align="right">26.66</td>
    <td align="right">27.17</td>
    <td align="right">28.05</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.87</td>
    <td align="right">31.58</td>
    <td align="right">31.79</td>
    <td align="right">32.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.21</td>
    <td align="right">41.03</td>
    <td align="right">41.33</td>
    <td align="right">40.96</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.51</td>
    <td align="right">41.92</td>
    <td align="right">41.12</td>
    <td align="right">41.31</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.52</td>
    <td align="right">28.43</td>
    <td align="right">28.06</td>
    <td align="right">28.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.34</td>
    <td align="right">55.86</td>
    <td align="right">55.19</td>
    <td align="right">55.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">31.90</td>
    <td align="right">55.77</td>
    <td align="right">55.53</td>
    <td align="right">55.79</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.75</td>
    <td align="right">37.25</td>
    <td align="right">27.45</td>
    <td align="right">29.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.53</td>
    <td align="right">76.97</td>
    <td align="right">77.06</td>
    <td align="right">76.95</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.75</td>
    <td align="right">77.12</td>
    <td align="right">77.08</td>
    <td align="right">77.00</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.12</td>
    <td align="right">53.47</td>
    <td align="right">36.95</td>
    <td align="right">38.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.04</td>
    <td align="right">84.02</td>
    <td align="right">83.98</td>
    <td align="right">83.83</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.01</td>
    <td align="right">90.64</td>
    <td align="right">89.38</td>
    <td align="right">89.29</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.21</td>
    <td align="right">53.93</td>
    <td align="right">37.37</td>
    <td align="right">39.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.87</td>
    <td align="right">27.85</td>
    <td align="right">27.83</td>
    <td align="right">27.85</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.72</td>
    <td align="right">30.16</td>
    <td align="right">30.16</td>
    <td align="right">30.25</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.30</td>
    <td align="right">30.70</td>
    <td align="right">30.54</td>
    <td align="right">30.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.91</td>
    <td align="right">43.77</td>
    <td align="right">34.38</td>
    <td align="right">35.85</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.79</td>
    <td align="right">38.51</td>
    <td align="right">28.98</td>
    <td align="right">30.66</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.65</td>
    <td align="right">47.74</td>
    <td align="right">37.67</td>
    <td align="right">38.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.12</td>
    <td align="right">53.15</td>
    <td align="right">36.47</td>
    <td align="right">38.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.88</td>
    <td align="right">57.58</td>
    <td align="right">39.72</td>
    <td align="right">41.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.70</td>
    <td align="right">57.03</td>
    <td align="right">39.44</td>
    <td align="right">41.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.09</td>
    <td align="right">53.66</td>
    <td align="right">36.82</td>
    <td align="right">38.89</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.66</td>
    <td align="right">59.47</td>
    <td align="right">40.13</td>
    <td align="right">42.40</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.97</td>
    <td align="right">58.73</td>
    <td align="right">39.82</td>
    <td align="right">42.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">26.89</td>
    <td align="right">44.26</td>
    <td align="right">33.29</td>
    <td align="right">35.71</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.46</td>
    <td align="right">55.48</td>
    <td align="right">36.65</td>
    <td align="right">38.42</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.07</td>
    <td align="right">60.46</td>
    <td align="right">60.51</td>
    <td align="right">60.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.54</td>
    <td align="right">62.42</td>
    <td align="right">33.29</td>
    <td align="right">37.12</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.92</td>
    <td align="right">63.19</td>
    <td align="right">35.24</td>
    <td align="right">38.98</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.39</td>
    <td align="right">78.68</td>
    <td align="right">78.46</td>
    <td align="right">78.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.74</td>
    <td align="right">73.74</td>
    <td align="right">32.86</td>
    <td align="right">38.03</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.74</td>
    <td align="right">80.06</td>
    <td align="right">37.20</td>
    <td align="right">42.58</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.92</td>
    <td align="right">84.25</td>
    <td align="right">84.11</td>
    <td align="right">84.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.12</td>
    <td align="right">101.72</td>
    <td align="right">35.53</td>
    <td align="right">43.71</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.19</td>
    <td align="right">101.67</td>
    <td align="right">37.61</td>
    <td align="right">45.85</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.73</td>
    <td align="right">118.19</td>
    <td align="right">118.14</td>
    <td align="right">118.54</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.13</td>
    <td align="right">33.36</td>
    <td align="right">15.82</td>
    <td align="right">23.94</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.05</td>
    <td align="right">61.61</td>
    <td align="right">41.32</td>
    <td align="right">44.37</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">20.91</td>
    <td align="right">20.55</td>
    <td align="right">23.59</td>
    <td align="right">24.61</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.64</td>
    <td align="right">26.74</td>
    <td align="right">28.12</td>
    <td align="right">29.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">130.75</td>
    <td align="right">117.88</td>
    <td align="right">50.94</td>
    <td align="right">56.94</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.65</td>
    <td align="right">24.15</td>
    <td align="right">25.99</td>
    <td align="right">27.15</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.07</td>
    <td align="right">30.87</td>
    <td align="right">31.42</td>
    <td align="right">32.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">263.00</td>
    <td align="right">215.93</td>
    <td align="right">63.24</td>
    <td align="right">80.44</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.74</td>
    <td align="right">37.96</td>
    <td align="right">38.47</td>
    <td align="right">39.36</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.39</td>
    <td align="right">49.56</td>
    <td align="right">49.06</td>
    <td align="right">49.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">440.72</td>
    <td align="right">350.00</td>
    <td align="right">78.80</td>
    <td align="right">107.10</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.47</td>
    <td align="right">44.68</td>
    <td align="right">45.47</td>
    <td align="right">46.59</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.69</td>
    <td align="right">62.73</td>
    <td align="right">62.94</td>
    <td align="right">63.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.02</td>
    <td align="right">41.45</td>
    <td align="right">41.88</td>
    <td align="right">41.64</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.80</td>
    <td align="right">42.17</td>
    <td align="right">41.52</td>
    <td align="right">41.78</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.22</td>
    <td align="right">30.34</td>
    <td align="right">30.34</td>
    <td align="right">30.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.75</td>
    <td align="right">57.72</td>
    <td align="right">57.47</td>
    <td align="right">57.09</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.16</td>
    <td align="right">58.54</td>
    <td align="right">58.58</td>
    <td align="right">58.59</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.05</td>
    <td align="right">40.82</td>
    <td align="right">30.87</td>
    <td align="right">32.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.46</td>
    <td align="right">90.53</td>
    <td align="right">90.66</td>
    <td align="right">90.58</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.31</td>
    <td align="right">93.31</td>
    <td align="right">93.36</td>
    <td align="right">93.27</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.34</td>
    <td align="right">78.41</td>
    <td align="right">61.72</td>
    <td align="right">63.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.31</td>
    <td align="right">107.41</td>
    <td align="right">107.39</td>
    <td align="right">107.46</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.16</td>
    <td align="right">119.47</td>
    <td align="right">118.40</td>
    <td align="right">118.44</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">59.22</td>
    <td align="right">90.20</td>
    <td align="right">74.95</td>
    <td align="right">76.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.13</td>
    <td align="right">29.92</td>
    <td align="right">29.90</td>
    <td align="right">29.94</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.14</td>
    <td align="right">32.05</td>
    <td align="right">31.99</td>
    <td align="right">32.02</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.46</td>
    <td align="right">31.86</td>
    <td align="right">31.85</td>
    <td align="right">31.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.20</td>
    <td align="right">48.31</td>
    <td align="right">38.24</td>
    <td align="right">40.51</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.14</td>
    <td align="right">41.38</td>
    <td align="right">31.38</td>
    <td align="right">32.87</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">24.11</td>
    <td align="right">52.08</td>
    <td align="right">41.99</td>
    <td align="right">43.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.41</td>
    <td align="right">78.24</td>
    <td align="right">62.41</td>
    <td align="right">65.02</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">51.89</td>
    <td align="right">80.83</td>
    <td align="right">63.02</td>
    <td align="right">65.39</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.50</td>
    <td align="right">80.74</td>
    <td align="right">62.95</td>
    <td align="right">65.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.18</td>
    <td align="right">92.43</td>
    <td align="right">76.15</td>
    <td align="right">78.20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.47</td>
    <td align="right">97.77</td>
    <td align="right">77.58</td>
    <td align="right">79.77</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.85</td>
    <td align="right">98.34</td>
    <td align="right">77.98</td>
    <td align="right">80.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lpk.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.72</td>
    <td align="right">44.49</td>
    <td align="right">35.09</td>
    <td align="right">37.40</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.25</td>
    <td align="right">55.77</td>
    <td align="right">39.00</td>
    <td align="right">40.61</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.29</td>
    <td align="right">60.78</td>
    <td align="right">60.79</td>
    <td align="right">60.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.71</td>
    <td align="right">65.76</td>
    <td align="right">37.40</td>
    <td align="right">41.45</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">45.63</td>
    <td align="right">65.97</td>
    <td align="right">39.09</td>
    <td align="right">43.13</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.21</td>
    <td align="right">79.53</td>
    <td align="right">79.68</td>
    <td align="right">79.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">59.03</td>
    <td align="right">87.29</td>
    <td align="right">50.20</td>
    <td align="right">55.39</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.53</td>
    <td align="right">101.14</td>
    <td align="right">60.90</td>
    <td align="right">66.39</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.49</td>
    <td align="right">104.30</td>
    <td align="right">104.38</td>
    <td align="right">104.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">79.99</td>
    <td align="right">123.63</td>
    <td align="right">63.38</td>
    <td align="right">70.69</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.37</td>
    <td align="right">134.78</td>
    <td align="right">74.77</td>
    <td align="right">82.31</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">108.67</td>
    <td align="right">145.77</td>
    <td align="right">145.90</td>
    <td align="right">145.73</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
