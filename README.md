# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.82</td>
    <td align="right">4.36</td>
    <td align="right">3.46</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.17</td>
    <td align="right">10.64</td>
    <td align="right">16.67</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.98</td>
    <td align="right">4.33</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.82</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.51</td>
    <td align="right">15.63</td>
    <td align="right">17.69</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.78</td>
    <td align="right">4.93</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.49</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.25</td>
    <td align="right">18.43</td>
    <td align="right">16.44</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.36</td>
    <td align="right">5.27</td>
    <td align="right">5.12</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.21</td>
    <td align="right">6.37</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.08</td>
    <td align="right">22.75</td>
    <td align="right">16.76</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.15</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.67</td>
    <td align="right">6.55</td>
    <td align="right">6.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.04</td>
    <td align="right">5.70</td>
    <td align="right">5.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.22</td>
    <td align="right">6.54</td>
    <td align="right">6.50</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.90</td>
    <td align="right">3.23</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.49</td>
    <td align="right">8.85</td>
    <td align="right">8.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.13</td>
    <td align="right">9.77</td>
    <td align="right">9.80</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.17</td>
    <td align="right">13.20</td>
    <td align="right">13.20</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.70</td>
    <td align="right">14.99</td>
    <td align="right">15.04</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.70</td>
    <td align="right">5.72</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.95</td>
    <td align="right">14.95</td>
    <td align="right">14.97</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.14</td>
    <td align="right">16.14</td>
    <td align="right">16.26</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.74</td>
    <td align="right">5.72</td>
    <td align="right">3.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.91</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.35</td>
    <td align="right">5.06</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.54</td>
    <td align="right">4.92</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.00</td>
    <td align="right">3.28</td>
    <td align="right">3.28</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.18</td>
    <td align="right">4.44</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.41</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.37</td>
    <td align="right">5.41</td>
    <td align="right">3.72</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.00</td>
    <td align="right">7.60</td>
    <td align="right">5.82</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.76</td>
    <td align="right">7.41</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.42</td>
    <td align="right">5.45</td>
    <td align="right">3.74</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.94</td>
    <td align="right">8.98</td>
    <td align="right">5.83</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.20</td>
    <td align="right">8.87</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.85</td>
    <td align="right">6.97</td>
    <td align="right">13.55</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.41</td>
    <td align="right">8.88</td>
    <td align="right">17.32</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.77</td>
    <td align="right">10.90</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.25</td>
    <td align="right">8.14</td>
    <td align="right">12.43</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.08</td>
    <td align="right">9.42</td>
    <td align="right">14.29</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.19</td>
    <td align="right">15.33</td>
    <td align="right">15.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.91</td>
    <td align="right">10.32</td>
    <td align="right">12.01</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.26</td>
    <td align="right">12.51</td>
    <td align="right">15.21</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.28</td>
    <td align="right">16.70</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.36</td>
    <td align="right">12.72</td>
    <td align="right">13.17</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.67</td>
    <td align="right">14.09</td>
    <td align="right">14.88</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.61</td>
    <td align="right">22.35</td>
    <td align="right">22.40</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.17</td>
    <td align="right">19.64</td>
    <td align="right">6.77</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.19</td>
    <td align="right">12.44</td>
    <td align="right">17.43</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.38</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.34</td>
    <td align="right">5.52</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.73</td>
    <td align="right">16.58</td>
    <td align="right">17.76</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.19</td>
    <td align="right">5.28</td>
    <td align="right">5.31</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.62</td>
    <td align="right">5.66</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.38</td>
    <td align="right">24.61</td>
    <td align="right">17.34</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.60</td>
    <td align="right">6.34</td>
    <td align="right">6.32</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.23</td>
    <td align="right">7.45</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">39.12</td>
    <td align="right">35.34</td>
    <td align="right">19.11</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.43</td>
    <td align="right">7.95</td>
    <td align="right">8.25</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.83</td>
    <td align="right">8.63</td>
    <td align="right">8.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.80</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.72</td>
    <td align="right">7.35</td>
    <td align="right">7.29</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.43</td>
    <td align="right">3.88</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.77</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.61</td>
    <td align="right">10.43</td>
    <td align="right">10.45</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.78</td>
    <td align="right">3.39</td>
    <td align="right">3.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.29</td>
    <td align="right">14.44</td>
    <td align="right">14.42</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.59</td>
    <td align="right">16.57</td>
    <td align="right">16.69</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.84</td>
    <td align="right">7.05</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.29</td>
    <td align="right">17.81</td>
    <td align="right">17.44</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.71</td>
    <td align="right">19.15</td>
    <td align="right">19.60</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">6.58</td>
    <td align="right">6.24</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.23</td>
    <td align="right">3.52</td>
    <td align="right">3.53</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.90</td>
    <td align="right">5.65</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.88</td>
    <td align="right">5.17</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.21</td>
    <td align="right">3.50</td>
    <td align="right">3.49</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.27</td>
    <td align="right">4.50</td>
    <td align="right">4.48</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.78</td>
    <td align="right">5.53</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.10</td>
    <td align="right">6.51</td>
    <td align="right">4.57</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.11</td>
    <td align="right">9.72</td>
    <td align="right">7.67</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">8.80</td>
    <td align="right">8.70</td>
    <td align="right">6.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.90</td>
    <td align="right">10.54</td>
    <td align="right">6.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.39</td>
    <td align="right">12.10</td>
    <td align="right">8.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.64</td>
    <td align="right">11.79</td>
    <td align="right">8.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.85</td>
    <td align="right">7.95</td>
    <td align="right">13.94</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.26</td>
    <td align="right">9.86</td>
    <td align="right">17.96</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.76</td>
    <td align="right">12.95</td>
    <td align="right">12.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.78</td>
    <td align="right">8.58</td>
    <td align="right">12.67</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.04</td>
    <td align="right">10.28</td>
    <td align="right">14.73</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.81</td>
    <td align="right">17.48</td>
    <td align="right">17.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.68</td>
    <td align="right">12.07</td>
    <td align="right">12.83</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">17.63</td>
    <td align="right">14.57</td>
    <td align="right">15.96</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">20.34</td>
    <td align="right">20.44</td>
    <td align="right">20.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">18.71</td>
    <td align="right">15.85</td>
    <td align="right">14.78</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">24.58</td>
    <td align="right">19.21</td>
    <td align="right">16.90</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">29.64</td>
    <td align="right">29.33</td>
    <td align="right">29.35</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.25</td>
    <td align="right">4.34</td>
    <td align="right">3.78</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.37</td>
    <td align="right">9.06</td>
    <td align="right">15.45</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.72</td>
    <td align="right">4.01</td>
    <td align="right">4.12</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.50</td>
    <td align="right">13.80</td>
    <td align="right">16.77</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.11</td>
    <td align="right">4.61</td>
    <td align="right">4.63</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.55</td>
    <td align="right">5.36</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.54</td>
    <td align="right">16.95</td>
    <td align="right">15.98</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.55</td>
    <td align="right">5.13</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.71</td>
    <td align="right">6.04</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.51</td>
    <td align="right">23.05</td>
    <td align="right">16.03</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.65</td>
    <td align="right">5.77</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.93</td>
    <td align="right">3.37</td>
    <td align="right">3.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.12</td>
    <td align="right">3.66</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.25</td>
    <td align="right">3.60</td>
    <td align="right">3.57</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.65</td>
    <td align="right">2.57</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.79</td>
    <td align="right">4.14</td>
    <td align="right">4.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.83</td>
    <td align="right">4.44</td>
    <td align="right">4.50</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.18</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.64</td>
    <td align="right">7.26</td>
    <td align="right">7.28</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.90</td>
    <td align="right">7.13</td>
    <td align="right">7.13</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.25</td>
    <td align="right">4.45</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.11</td>
    <td align="right">7.68</td>
    <td align="right">7.69</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.01</td>
    <td align="right">7.77</td>
    <td align="right">7.73</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.30</td>
    <td align="right">4.48</td>
    <td align="right">3.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.63</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.70</td>
    <td align="right">4.14</td>
    <td align="right">4.15</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.74</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.77</td>
    <td align="right">2.46</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.00</td>
    <td align="right">3.79</td>
    <td align="right">3.79</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.94</td>
    <td align="right">4.14</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.34</td>
    <td align="right">4.38</td>
    <td align="right">2.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.78</td>
    <td align="right">6.17</td>
    <td align="right">4.77</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.89</td>
    <td align="right">6.11</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.34</td>
    <td align="right">4.38</td>
    <td align="right">3.00</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.73</td>
    <td align="right">7.30</td>
    <td align="right">4.86</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.91</td>
    <td align="right">7.20</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.91</td>
    <td align="right">6.16</td>
    <td align="right">12.24</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.39</td>
    <td align="right">8.12</td>
    <td align="right">16.45</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.85</td>
    <td align="right">11.34</td>
    <td align="right">11.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.56</td>
    <td align="right">8.26</td>
    <td align="right">12.27</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.30</td>
    <td align="right">9.71</td>
    <td align="right">13.95</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.31</td>
    <td align="right">16.80</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.77</td>
    <td align="right">10.08</td>
    <td align="right">11.85</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.54</td>
    <td align="right">12.56</td>
    <td align="right">14.81</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">19.57</td>
    <td align="right">19.71</td>
    <td align="right">19.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">15.03</td>
    <td align="right">12.43</td>
    <td align="right">12.58</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.33</td>
    <td align="right">14.00</td>
    <td align="right">14.34</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">26.97</td>
    <td align="right">26.79</td>
    <td align="right">25.89</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.12</td>
    <td align="right">17.50</td>
    <td align="right">9.08</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.65</td>
    <td align="right">9.92</td>
    <td align="right">16.21</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.59</td>
    <td align="right">4.82</td>
    <td align="right">5.33</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.99</td>
    <td align="right">5.27</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.86</td>
    <td align="right">17.04</td>
    <td align="right">17.57</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.45</td>
    <td align="right">5.99</td>
    <td align="right">6.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.78</td>
    <td align="right">5.98</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">32.11</td>
    <td align="right">32.96</td>
    <td align="right">19.64</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.12</td>
    <td align="right">13.60</td>
    <td align="right">13.43</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.64</td>
    <td align="right">13.42</td>
    <td align="right">13.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">74.70</td>
    <td align="right">81.66</td>
    <td align="right">26.83</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">23.29</td>
    <td align="right">20.41</td>
    <td align="right">19.96</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.81</td>
    <td align="right">11.42</td>
    <td align="right">13.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.94</td>
    <td align="right">4.30</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.81</td>
    <td align="right">4.33</td>
    <td align="right">4.84</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.26</td>
    <td align="right">3.28</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.17</td>
    <td align="right">10.28</td>
    <td align="right">11.43</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.47</td>
    <td align="right">8.79</td>
    <td align="right">8.69</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.91</td>
    <td align="right">4.67</td>
    <td align="right">4.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.99</td>
    <td align="right">21.19</td>
    <td align="right">20.94</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.79</td>
    <td align="right">17.40</td>
    <td align="right">20.11</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.70</td>
    <td align="right">16.01</td>
    <td align="right">10.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.99</td>
    <td align="right">24.96</td>
    <td align="right">24.99</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">19.12</td>
    <td align="right">28.43</td>
    <td align="right">28.54</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.40</td>
    <td align="right">15.48</td>
    <td align="right">9.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.00</td>
    <td align="right">2.74</td>
    <td align="right">2.75</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.43</td>
    <td align="right">5.01</td>
    <td align="right">4.94</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.38</td>
    <td align="right">4.42</td>
    <td align="right">4.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.08</td>
    <td align="right">2.81</td>
    <td align="right">2.79</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">7.26</td>
    <td align="right">9.76</td>
    <td align="right">10.27</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">6.18</td>
    <td align="right">7.97</td>
    <td align="right">9.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">11.74</td>
    <td align="right">12.58</td>
    <td align="right">7.57</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">11.62</td>
    <td align="right">12.97</td>
    <td align="right">10.02</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">15.21</td>
    <td align="right">17.28</td>
    <td align="right">11.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">15.65</td>
    <td align="right">17.62</td>
    <td align="right">12.24</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">22.30</td>
    <td align="right">26.03</td>
    <td align="right">16.78</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">22.70</td>
    <td align="right">27.41</td>
    <td align="right">15.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.14</td>
    <td align="right">7.97</td>
    <td align="right">15.19</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">17.20</td>
    <td align="right">12.76</td>
    <td align="right">20.06</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">18.03</td>
    <td align="right">18.47</td>
    <td align="right">18.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">29.27</td>
    <td align="right">17.41</td>
    <td align="right">17.61</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">30.66</td>
    <td align="right">25.21</td>
    <td align="right">17.78</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.65</td>
    <td align="right">22.53</td>
    <td align="right">22.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">32.33</td>
    <td align="right">29.90</td>
    <td align="right">19.17</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">38.80</td>
    <td align="right">35.31</td>
    <td align="right">20.42</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">27.13</td>
    <td align="right">27.34</td>
    <td align="right">27.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">48.24</td>
    <td align="right">36.37</td>
    <td align="right">20.52</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">61.56</td>
    <td align="right">41.52</td>
    <td align="right">21.64</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">46.05</td>
    <td align="right">46.97</td>
    <td align="right">48.60</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">22.28</td>
    <td align="right">5.20</td>
    <td align="right">3.44</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.28</td>
    <td align="right">5.11</td>
    <td align="right">13.32</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.50</td>
    <td align="right">2.35</td>
    <td align="right">1.44</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.99</td>
    <td align="right">1.63</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.88</td>
    <td align="right">8.08</td>
    <td align="right">13.38</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">2.15</td>
    <td align="right">1.87</td>
    <td align="right">1.61</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.15</td>
    <td align="right">2.05</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.38</td>
    <td align="right">10.08</td>
    <td align="right">13.32</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.98</td>
    <td align="right">2.12</td>
    <td align="right">2.01</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.88</td>
    <td align="right">2.10</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">22.67</td>
    <td align="right">14.21</td>
    <td align="right">13.08</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.79</td>
    <td align="right">3.23</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.27</td>
    <td align="right">2.32</td>
    <td align="right">1.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.10</td>
    <td align="right">2.04</td>
    <td align="right">2.80</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.86</td>
    <td align="right">2.19</td>
    <td align="right">2.45</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.37</td>
    <td align="right">3.05</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.63</td>
    <td align="right">3.83</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.42</td>
    <td align="right">3.06</td>
    <td align="right">2.66</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.83</td>
    <td align="right">2.29</td>
    <td align="right">1.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.78</td>
    <td align="right">3.77</td>
    <td align="right">3.74</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.51</td>
    <td align="right">4.31</td>
    <td align="right">4.16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.62</td>
    <td align="right">5.68</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.16</td>
    <td align="right">4.46</td>
    <td align="right">4.75</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.71</td>
    <td align="right">4.61</td>
    <td align="right">5.41</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.37</td>
    <td align="right">4.33</td>
    <td align="right">2.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.97</td>
    <td align="right">2.91</td>
    <td align="right">2.33</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.26</td>
    <td align="right">2.15</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.22</td>
    <td align="right">2.36</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.20</td>
    <td align="right">2.73</td>
    <td align="right">2.80</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.24</td>
    <td align="right">2.02</td>
    <td align="right">2.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.57</td>
    <td align="right">3.53</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.29</td>
    <td align="right">3.16</td>
    <td align="right">2.25</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.36</td>
    <td align="right">3.65</td>
    <td align="right">4.50</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.42</td>
    <td align="right">4.12</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.84</td>
    <td align="right">4.85</td>
    <td align="right">2.48</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.37</td>
    <td align="right">5.58</td>
    <td align="right">5.51</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.18</td>
    <td align="right">7.09</td>
    <td align="right">8.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">5.28</td>
    <td align="right">4.09</td>
    <td align="right">14.83</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">13.48</td>
    <td align="right">5.98</td>
    <td align="right">16.72</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.12</td>
    <td align="right">6.06</td>
    <td align="right">7.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.37</td>
    <td align="right">5.79</td>
    <td align="right">12.70</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.57</td>
    <td align="right">6.55</td>
    <td align="right">15.08</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.34</td>
    <td align="right">9.53</td>
    <td align="right">11.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.87</td>
    <td align="right">10.95</td>
    <td align="right">13.73</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">17.87</td>
    <td align="right">7.48</td>
    <td align="right">16.04</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">17.49</td>
    <td align="right">12.24</td>
    <td align="right">14.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.80</td>
    <td align="right">13.03</td>
    <td align="right">13.87</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">15.35</td>
    <td align="right">12.28</td>
    <td align="right">19.28</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">25.01</td>
    <td align="right">13.47</td>
    <td align="right">16.10</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.25</td>
    <td align="right">18.69</td>
    <td align="right">13.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">17.48</td>
    <td align="right">20.49</td>
    <td align="right">28.79</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">8.31</td>
    <td align="right">7.59</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.03</td>
    <td align="right">6.74</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">47.54</td>
    <td align="right">39.75</td>
    <td align="right">32.99</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.25</td>
    <td align="right">10.69</td>
    <td align="right">12.04</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.77</td>
    <td align="right">10.46</td>
    <td align="right">9.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">73.89</td>
    <td align="right">45.58</td>
    <td align="right">25.19</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.25</td>
    <td align="right">9.12</td>
    <td align="right">9.16</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.17</td>
    <td align="right">14.88</td>
    <td align="right">14.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">119.21</td>
    <td align="right">91.12</td>
    <td align="right">36.96</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.12</td>
    <td align="right">13.22</td>
    <td align="right">10.80</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.64</td>
    <td align="right">13.14</td>
    <td align="right">11.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.05</td>
    <td align="right">6.36</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.21</td>
    <td align="right">5.96</td>
    <td align="right">8.98</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.34</td>
    <td align="right">5.34</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.55</td>
    <td align="right">9.66</td>
    <td align="right">9.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.57</td>
    <td align="right">9.65</td>
    <td align="right">9.97</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.57</td>
    <td align="right">7.12</td>
    <td align="right">9.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.00</td>
    <td align="right">17.68</td>
    <td align="right">18.04</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.02</td>
    <td align="right">16.00</td>
    <td align="right">15.80</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.83</td>
    <td align="right">13.67</td>
    <td align="right">7.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.90</td>
    <td align="right">18.30</td>
    <td align="right">19.33</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.09</td>
    <td align="right">21.95</td>
    <td align="right">20.51</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">15.13</td>
    <td align="right">16.56</td>
    <td align="right">8.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">5.94</td>
    <td align="right">6.02</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.46</td>
    <td align="right">7.03</td>
    <td align="right">4.53</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.94</td>
    <td align="right">5.25</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">6.31</td>
    <td align="right">5.98</td>
    <td align="right">7.77</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.48</td>
    <td align="right">8.92</td>
    <td align="right">9.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.25</td>
    <td align="right">8.30</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">12.06</td>
    <td align="right">12.43</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.97</td>
    <td align="right">14.83</td>
    <td align="right">14.52</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.60</td>
    <td align="right">16.60</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">15.68</td>
    <td align="right">14.25</td>
    <td align="right">7.38</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">19.23</td>
    <td align="right">15.65</td>
    <td align="right">16.19</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.96</td>
    <td align="right">20.32</td>
    <td align="right">20.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.21</td>
    <td align="right">10.26</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">15.63</td>
    <td align="right">7.37</td>
    <td align="right">18.03</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">10.39</td>
    <td align="right">8.79</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.64</td>
    <td align="right">12.84</td>
    <td align="right">15.22</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">18.35</td>
    <td align="right">11.13</td>
    <td align="right">16.21</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.64</td>
    <td align="right">17.84</td>
    <td align="right">15.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">22.53</td>
    <td align="right">17.14</td>
    <td align="right">14.56</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">25.10</td>
    <td align="right">17.63</td>
    <td align="right">17.09</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.53</td>
    <td align="right">25.94</td>
    <td align="right">23.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">25.46</td>
    <td align="right">20.79</td>
    <td align="right">16.25</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">34.68</td>
    <td align="right">28.03</td>
    <td align="right">19.82</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">52.35</td>
    <td align="right">50.52</td>
    <td align="right">50.43</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.54</td>
    <td align="right">5.71</td>
    <td align="right">4.76</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.02</td>
    <td align="right">12.50</td>
    <td align="right">16.92</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.81</td>
    <td align="right">4.22</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">5.22</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.28</td>
    <td align="right">17.55</td>
    <td align="right">17.65</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.88</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.44</td>
    <td align="right">21.17</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.58</td>
    <td align="right">5.42</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.29</td>
    <td align="right">6.52</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.75</td>
    <td align="right">26.95</td>
    <td align="right">17.52</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">5.89</td>
    <td align="right">5.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.33</td>
    <td align="right">7.37</td>
    <td align="right">7.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.82</td>
    <td align="right">5.55</td>
    <td align="right">5.65</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.10</td>
    <td align="right">5.53</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.35</td>
    <td align="right">3.93</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.58</td>
    <td align="right">8.13</td>
    <td align="right">8.13</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.58</td>
    <td align="right">8.64</td>
    <td align="right">7.83</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.86</td>
    <td align="right">4.82</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">14.98</td>
    <td align="right">10.96</td>
    <td align="right">10.77</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">24.41</td>
    <td align="right">10.47</td>
    <td align="right">10.38</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.99</td>
    <td align="right">7.01</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.76</td>
    <td align="right">12.55</td>
    <td align="right">12.55</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">21.82</td>
    <td align="right">13.41</td>
    <td align="right">13.35</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.04</td>
    <td align="right">7.05</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.25</td>
    <td align="right">3.82</td>
    <td align="right">3.81</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.55</td>
    <td align="right">5.49</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.65</td>
    <td align="right">5.41</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.29</td>
    <td align="right">5.49</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.75</td>
    <td align="right">5.77</td>
    <td align="right">4.98</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">7.05</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.05</td>
    <td align="right">6.75</td>
    <td align="right">4.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.78</td>
    <td align="right">9.24</td>
    <td align="right">7.47</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.60</td>
    <td align="right">9.25</td>
    <td align="right">7.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.15</td>
    <td align="right">6.85</td>
    <td align="right">5.05</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.30</td>
    <td align="right">10.75</td>
    <td align="right">7.76</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.02</td>
    <td align="right">10.53</td>
    <td align="right">7.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.62</td>
    <td align="right">9.44</td>
    <td align="right">13.67</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.27</td>
    <td align="right">11.62</td>
    <td align="right">17.06</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.67</td>
    <td align="right">10.62</td>
    <td align="right">10.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.76</td>
    <td align="right">10.91</td>
    <td align="right">12.95</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.45</td>
    <td align="right">12.88</td>
    <td align="right">14.50</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">18.47</td>
    <td align="right">15.61</td>
    <td align="right">15.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.27</td>
    <td align="right">14.09</td>
    <td align="right">12.67</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.05</td>
    <td align="right">17.48</td>
    <td align="right">15.25</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">22.05</td>
    <td align="right">18.31</td>
    <td align="right">18.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.36</td>
    <td align="right">17.43</td>
    <td align="right">13.95</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.54</td>
    <td align="right">20.50</td>
    <td align="right">14.81</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">29.37</td>
    <td align="right">26.57</td>
    <td align="right">27.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.53</td>
    <td align="right">21.59</td>
    <td align="right">7.00</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.31</td>
    <td align="right">12.90</td>
    <td align="right">17.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.95</td>
    <td align="right">4.49</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.87</td>
    <td align="right">5.53</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.86</td>
    <td align="right">18.64</td>
    <td align="right">18.41</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.48</td>
    <td align="right">5.02</td>
    <td align="right">5.04</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.12</td>
    <td align="right">6.30</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.33</td>
    <td align="right">23.20</td>
    <td align="right">17.21</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.91</td>
    <td align="right">5.71</td>
    <td align="right">5.73</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.32</td>
    <td align="right">7.11</td>
    <td align="right">7.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">38.04</td>
    <td align="right">34.79</td>
    <td align="right">18.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.65</td>
    <td align="right">7.74</td>
    <td align="right">7.78</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.35</td>
    <td align="right">8.58</td>
    <td align="right">8.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.26</td>
    <td align="right">6.22</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.45</td>
    <td align="right">6.24</td>
    <td align="right">6.30</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.75</td>
    <td align="right">4.18</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.70</td>
    <td align="right">9.48</td>
    <td align="right">9.47</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.41</td>
    <td align="right">9.41</td>
    <td align="right">8.74</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.27</td>
    <td align="right">5.21</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.52</td>
    <td align="right">12.74</td>
    <td align="right">12.46</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">24.45</td>
    <td align="right">11.39</td>
    <td align="right">11.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.54</td>
    <td align="right">7.59</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">19.96</td>
    <td align="right">16.02</td>
    <td align="right">16.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.35</td>
    <td align="right">15.23</td>
    <td align="right">15.07</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.67</td>
    <td align="right">9.13</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.68</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.00</td>
    <td align="right">5.86</td>
    <td align="right">5.86</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.18</td>
    <td align="right">5.72</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.76</td>
    <td align="right">5.90</td>
    <td align="right">5.04</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.39</td>
    <td align="right">6.22</td>
    <td align="right">5.40</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.52</td>
    <td align="right">7.58</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.86</td>
    <td align="right">7.29</td>
    <td align="right">5.44</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.65</td>
    <td align="right">9.88</td>
    <td align="right">8.11</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.51</td>
    <td align="right">10.05</td>
    <td align="right">8.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.24</td>
    <td align="right">8.99</td>
    <td align="right">6.89</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.50</td>
    <td align="right">16.32</td>
    <td align="right">12.48</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.22</td>
    <td align="right">13.23</td>
    <td align="right">9.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.61</td>
    <td align="right">9.54</td>
    <td align="right">13.92</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.73</td>
    <td align="right">12.57</td>
    <td align="right">17.57</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.57</td>
    <td align="right">14.19</td>
    <td align="right">15.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.74</td>
    <td align="right">12.10</td>
    <td align="right">13.29</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.94</td>
    <td align="right">13.91</td>
    <td align="right">14.91</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">21.36</td>
    <td align="right">20.72</td>
    <td align="right">20.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.64</td>
    <td align="right">15.52</td>
    <td align="right">13.08</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.76</td>
    <td align="right">19.77</td>
    <td align="right">16.07</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">27.23</td>
    <td align="right">20.62</td>
    <td align="right">26.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.48</td>
    <td align="right">19.57</td>
    <td align="right">14.81</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">25.39</td>
    <td align="right">25.19</td>
    <td align="right">16.29</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">35.52</td>
    <td align="right">42.18</td>
    <td align="right">35.81</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.35</td>
    <td align="right">30.19</td>
    <td align="right">13.86</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.41</td>
    <td align="right">41.79</td>
    <td align="right">36.00</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.48</td>
    <td align="right">15.57</td>
    <td align="right">15.58</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.20</td>
    <td align="right">19.10</td>
    <td align="right">19.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.34</td>
    <td align="right">64.34</td>
    <td align="right">39.22</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.37</td>
    <td align="right">19.50</td>
    <td align="right">19.56</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.17</td>
    <td align="right">18.55</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.93</td>
    <td align="right">78.14</td>
    <td align="right">38.59</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.40</td>
    <td align="right">18.42</td>
    <td align="right">18.52</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.08</td>
    <td align="right">18.34</td>
    <td align="right">18.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.85</td>
    <td align="right">96.57</td>
    <td align="right">37.17</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.26</td>
    <td align="right">18.77</td>
    <td align="right">18.75</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.93</td>
    <td align="right">19.88</td>
    <td align="right">19.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.20</td>
    <td align="right">21.30</td>
    <td align="right">21.32</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.83</td>
    <td align="right">22.32</td>
    <td align="right">22.31</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.00</td>
    <td align="right">13.62</td>
    <td align="right">13.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.00</td>
    <td align="right">25.89</td>
    <td align="right">25.89</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.72</td>
    <td align="right">27.91</td>
    <td align="right">27.93</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.05</td>
    <td align="right">16.29</td>
    <td align="right">15.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.11</td>
    <td align="right">33.42</td>
    <td align="right">33.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.90</td>
    <td align="right">46.79</td>
    <td align="right">47.03</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.91</td>
    <td align="right">19.40</td>
    <td align="right">19.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.73</td>
    <td align="right">36.25</td>
    <td align="right">36.25</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.91</td>
    <td align="right">56.67</td>
    <td align="right">56.70</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">22.70</td>
    <td align="right">25.51</td>
    <td align="right">25.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.36</td>
    <td align="right">15.59</td>
    <td align="right">15.56</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.26</td>
    <td align="right">21.30</td>
    <td align="right">21.27</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.92</td>
    <td align="right">22.38</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.82</td>
    <td align="right">20.31</td>
    <td align="right">20.28</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.02</td>
    <td align="right">25.93</td>
    <td align="right">25.93</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.81</td>
    <td align="right">27.97</td>
    <td align="right">27.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.52</td>
    <td align="right">24.71</td>
    <td align="right">24.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.05</td>
    <td align="right">33.43</td>
    <td align="right">33.41</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.85</td>
    <td align="right">46.80</td>
    <td align="right">47.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.36</td>
    <td align="right">37.26</td>
    <td align="right">37.29</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.66</td>
    <td align="right">36.20</td>
    <td align="right">36.18</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.94</td>
    <td align="right">56.62</td>
    <td align="right">56.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.24</td>
    <td align="right">20.85</td>
    <td align="right">25.52</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.25</td>
    <td align="right">29.35</td>
    <td align="right">34.73</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.75</td>
    <td align="right">30.32</td>
    <td align="right">30.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.18</td>
    <td align="right">28.32</td>
    <td align="right">26.28</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.85</td>
    <td align="right">33.53</td>
    <td align="right">30.54</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">37.24</td>
    <td align="right">38.74</td>
    <td align="right">39.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.67</td>
    <td align="right">33.64</td>
    <td align="right">25.70</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.16</td>
    <td align="right">41.78</td>
    <td align="right">33.54</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.18</td>
    <td align="right">41.39</td>
    <td align="right">41.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.54</td>
    <td align="right">40.12</td>
    <td align="right">26.85</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">49.11</td>
    <td align="right">43.92</td>
    <td align="right">31.37</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">54.59</td>
    <td align="right">58.49</td>
    <td align="right">58.35</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">69.47</td>
    <td align="right">98.37</td>
    <td align="right">17.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.74</td>
    <td align="right">42.92</td>
    <td align="right">38.99</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.79</td>
    <td align="right">15.57</td>
    <td align="right">15.59</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.43</td>
    <td align="right">19.16</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.17</td>
    <td align="right">64.12</td>
    <td align="right">40.69</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.93</td>
    <td align="right">20.41</td>
    <td align="right">21.15</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.64</td>
    <td align="right">18.97</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">48.50</td>
    <td align="right">108.90</td>
    <td align="right">46.03</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">19.37</td>
    <td align="right">20.56</td>
    <td align="right">20.82</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">21.02</td>
    <td align="right">21.23</td>
    <td align="right">21.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">98.92</td>
    <td align="right">146.09</td>
    <td align="right">49.68</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">25.33</td>
    <td align="right">31.58</td>
    <td align="right">29.90</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">36.57</td>
    <td align="right">29.65</td>
    <td align="right">29.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.39</td>
    <td align="right">22.36</td>
    <td align="right">22.42</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.89</td>
    <td align="right">23.17</td>
    <td align="right">23.41</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.26</td>
    <td align="right">14.24</td>
    <td align="right">14.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">23.80</td>
    <td align="right">27.54</td>
    <td align="right">26.41</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">54.59</td>
    <td align="right">31.12</td>
    <td align="right">30.07</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.02</td>
    <td align="right">17.47</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.66</td>
    <td align="right">42.47</td>
    <td align="right">42.30</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">86.96</td>
    <td align="right">54.14</td>
    <td align="right">63.28</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">18.33</td>
    <td align="right">26.45</td>
    <td align="right">21.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.76</td>
    <td align="right">56.97</td>
    <td align="right">76.06</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">109.22</td>
    <td align="right">71.84</td>
    <td align="right">70.34</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">39.68</td>
    <td align="right">54.44</td>
    <td align="right">42.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.86</td>
    <td align="right">16.22</td>
    <td align="right">16.49</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.74</td>
    <td align="right">22.01</td>
    <td align="right">22.36</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">34.32</td>
    <td align="right">23.29</td>
    <td align="right">23.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">20.28</td>
    <td align="right">22.47</td>
    <td align="right">23.77</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.99</td>
    <td align="right">26.28</td>
    <td align="right">30.31</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">51.12</td>
    <td align="right">33.08</td>
    <td align="right">30.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.28</td>
    <td align="right">36.66</td>
    <td align="right">41.54</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.09</td>
    <td align="right">50.06</td>
    <td align="right">45.69</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">76.84</td>
    <td align="right">52.57</td>
    <td align="right">69.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">68.85</td>
    <td align="right">76.08</td>
    <td align="right">67.61</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">70.21</td>
    <td align="right">77.79</td>
    <td align="right">72.78</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">101.63</td>
    <td align="right">83.90</td>
    <td align="right">88.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.70</td>
    <td align="right">21.74</td>
    <td align="right">26.36</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.42</td>
    <td align="right">30.17</td>
    <td align="right">37.33</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.34</td>
    <td align="right">32.75</td>
    <td align="right">32.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">33.82</td>
    <td align="right">32.64</td>
    <td align="right">27.52</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">64.55</td>
    <td align="right">39.44</td>
    <td align="right">35.35</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.55</td>
    <td align="right">40.85</td>
    <td align="right">41.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">41.15</td>
    <td align="right">52.36</td>
    <td align="right">34.54</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">80.57</td>
    <td align="right">92.88</td>
    <td align="right">48.41</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">45.82</td>
    <td align="right">44.58</td>
    <td align="right">47.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">81.25</td>
    <td align="right">80.54</td>
    <td align="right">44.07</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">108.41</td>
    <td align="right">104.62</td>
    <td align="right">51.07</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">57.08</td>
    <td align="right">62.19</td>
    <td align="right">62.62</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.06</td>
    <td align="right">10.80</td>
    <td align="right">7.62</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">14.00</td>
    <td align="right">23.09</td>
    <td align="right">26.75</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.54</td>
    <td align="right">12.50</td>
    <td align="right">12.71</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.83</td>
    <td align="right">13.91</td>
    <td align="right">13.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.62</td>
    <td align="right">35.22</td>
    <td align="right">29.58</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.79</td>
    <td align="right">14.12</td>
    <td align="right">14.17</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.80</td>
    <td align="right">15.37</td>
    <td align="right">15.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.25</td>
    <td align="right">47.57</td>
    <td align="right">29.54</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.93</td>
    <td align="right">15.47</td>
    <td align="right">15.56</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.43</td>
    <td align="right">16.82</td>
    <td align="right">16.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.18</td>
    <td align="right">60.32</td>
    <td align="right">31.13</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.30</td>
    <td align="right">16.39</td>
    <td align="right">16.37</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.43</td>
    <td align="right">17.94</td>
    <td align="right">17.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.85</td>
    <td align="right">16.33</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.61</td>
    <td align="right">16.92</td>
    <td align="right">16.89</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.17</td>
    <td align="right">9.50</td>
    <td align="right">9.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.46</td>
    <td align="right">22.57</td>
    <td align="right">22.56</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.20</td>
    <td align="right">22.37</td>
    <td align="right">22.28</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">9.34</td>
    <td align="right">14.18</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.01</td>
    <td align="right">32.29</td>
    <td align="right">32.29</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.92</td>
    <td align="right">31.03</td>
    <td align="right">31.03</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.68</td>
    <td align="right">17.60</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.25</td>
    <td align="right">36.34</td>
    <td align="right">36.07</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">35.98</td>
    <td align="right">35.95</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.42</td>
    <td align="right">20.46</td>
    <td align="right">20.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.57</td>
    <td align="right">9.43</td>
    <td align="right">9.42</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.74</td>
    <td align="right">16.18</td>
    <td align="right">16.19</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.27</td>
    <td align="right">16.80</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.02</td>
    <td align="right">13.69</td>
    <td align="right">13.69</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.43</td>
    <td align="right">22.39</td>
    <td align="right">22.39</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.02</td>
    <td align="right">22.31</td>
    <td align="right">22.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.00</td>
    <td align="right">17.64</td>
    <td align="right">17.65</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.03</td>
    <td align="right">32.21</td>
    <td align="right">32.19</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.77</td>
    <td align="right">31.26</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.22</td>
    <td align="right">20.96</td>
    <td align="right">20.83</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.06</td>
    <td align="right">35.82</td>
    <td align="right">35.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.09</td>
    <td align="right">35.89</td>
    <td align="right">36.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.24</td>
    <td align="right">16.31</td>
    <td align="right">19.94</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.60</td>
    <td align="right">32.84</td>
    <td align="right">36.51</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.75</td>
    <td align="right">24.37</td>
    <td align="right">24.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.00</td>
    <td align="right">23.59</td>
    <td align="right">20.92</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.65</td>
    <td align="right">38.47</td>
    <td align="right">36.63</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.16</td>
    <td align="right">32.07</td>
    <td align="right">32.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.19</td>
    <td align="right">30.38</td>
    <td align="right">20.71</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.09</td>
    <td align="right">45.46</td>
    <td align="right">37.76</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.15</td>
    <td align="right">35.50</td>
    <td align="right">35.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.19</td>
    <td align="right">35.88</td>
    <td align="right">21.42</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">67.04</td>
    <td align="right">48.09</td>
    <td align="right">37.39</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">42.71</td>
    <td align="right">46.33</td>
    <td align="right">46.35</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">84.20</td>
    <td align="right">47.87</td>
    <td align="right">12.07</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.36</td>
    <td align="right">22.95</td>
    <td align="right">28.18</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.48</td>
    <td align="right">12.50</td>
    <td align="right">12.49</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.37</td>
    <td align="right">14.04</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.08</td>
    <td align="right">34.16</td>
    <td align="right">29.44</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.77</td>
    <td align="right">14.33</td>
    <td align="right">13.75</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.33</td>
    <td align="right">14.86</td>
    <td align="right">14.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.21</td>
    <td align="right">49.18</td>
    <td align="right">29.30</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.35</td>
    <td align="right">14.91</td>
    <td align="right">15.51</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.61</td>
    <td align="right">16.63</td>
    <td align="right">23.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">35.07</td>
    <td align="right">81.08</td>
    <td align="right">33.37</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">31.81</td>
    <td align="right">35.47</td>
    <td align="right">37.97</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">22.25</td>
    <td align="right">29.08</td>
    <td align="right">29.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.73</td>
    <td align="right">17.04</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.36</td>
    <td align="right">17.44</td>
    <td align="right">17.44</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.16</td>
    <td align="right">9.43</td>
    <td align="right">9.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">19.96</td>
    <td align="right">23.10</td>
    <td align="right">23.86</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.84</td>
    <td align="right">24.49</td>
    <td align="right">25.85</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">9.49</td>
    <td align="right">15.03</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">27.46</td>
    <td align="right">38.48</td>
    <td align="right">37.73</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.76</td>
    <td align="right">33.81</td>
    <td align="right">38.95</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.36</td>
    <td align="right">23.06</td>
    <td align="right">22.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">45.39</td>
    <td align="right">51.91</td>
    <td align="right">36.43</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.29</td>
    <td align="right">38.14</td>
    <td align="right">39.68</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">20.57</td>
    <td align="right">25.65</td>
    <td align="right">21.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.73</td>
    <td align="right">9.49</td>
    <td align="right">9.50</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.70</td>
    <td align="right">16.55</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.33</td>
    <td align="right">17.39</td>
    <td align="right">17.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.14</td>
    <td align="right">13.43</td>
    <td align="right">13.87</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">19.43</td>
    <td align="right">26.78</td>
    <td align="right">27.28</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.89</td>
    <td align="right">22.25</td>
    <td align="right">24.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">19.97</td>
    <td align="right">31.53</td>
    <td align="right">39.96</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.73</td>
    <td align="right">54.81</td>
    <td align="right">59.58</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">41.24</td>
    <td align="right">50.13</td>
    <td align="right">52.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.32</td>
    <td align="right">58.24</td>
    <td align="right">58.17</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">83.58</td>
    <td align="right">96.98</td>
    <td align="right">93.86</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">93.72</td>
    <td align="right">96.48</td>
    <td align="right">94.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">34.52</td>
    <td align="right">45.64</td>
    <td align="right">32.75</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">109.88</td>
    <td align="right">80.25</td>
    <td align="right">70.16</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">22.49</td>
    <td align="right">27.04</td>
    <td align="right">27.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">57.26</td>
    <td align="right">73.07</td>
    <td align="right">39.61</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">130.14</td>
    <td align="right">110.87</td>
    <td align="right">70.49</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">32.89</td>
    <td align="right">36.75</td>
    <td align="right">37.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">96.26</td>
    <td align="right">100.34</td>
    <td align="right">43.02</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">121.13</td>
    <td align="right">107.58</td>
    <td align="right">66.29</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">38.57</td>
    <td align="right">47.94</td>
    <td align="right">43.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">85.37</td>
    <td align="right">95.57</td>
    <td align="right">43.71</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">136.68</td>
    <td align="right">118.53</td>
    <td align="right">71.18</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">82.49</td>
    <td align="right">89.79</td>
    <td align="right">75.32</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.46</td>
    <td align="right">8.51</td>
    <td align="right">6.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.39</td>
    <td align="right">54.96</td>
    <td align="right">41.54</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.01</td>
    <td align="right">19.64</td>
    <td align="right">23.26</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.85</td>
    <td align="right">21.57</td>
    <td align="right">24.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">88.95</td>
    <td align="right">80.29</td>
    <td align="right">43.92</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.16</td>
    <td align="right">21.30</td>
    <td align="right">23.79</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.20</td>
    <td align="right">22.40</td>
    <td align="right">24.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">109.71</td>
    <td align="right">100.49</td>
    <td align="right">44.37</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.15</td>
    <td align="right">22.65</td>
    <td align="right">24.35</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.58</td>
    <td align="right">24.17</td>
    <td align="right">25.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.42</td>
    <td align="right">125.39</td>
    <td align="right">45.24</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">26.97</td>
    <td align="right">24.27</td>
    <td align="right">25.37</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.72</td>
    <td align="right">25.62</td>
    <td align="right">26.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.06</td>
    <td align="right">41.32</td>
    <td align="right">41.36</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">28.68</td>
    <td align="right">41.65</td>
    <td align="right">41.18</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.71</td>
    <td align="right">25.44</td>
    <td align="right">25.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.80</td>
    <td align="right">56.32</td>
    <td align="right">56.89</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.51</td>
    <td align="right">57.76</td>
    <td align="right">57.92</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.54</td>
    <td align="right">36.17</td>
    <td align="right">25.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.39</td>
    <td align="right">76.93</td>
    <td align="right">76.97</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.46</td>
    <td align="right">77.78</td>
    <td align="right">77.84</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.97</td>
    <td align="right">54.94</td>
    <td align="right">39.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.85</td>
    <td align="right">86.16</td>
    <td align="right">86.05</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">49.63</td>
    <td align="right">92.25</td>
    <td align="right">92.26</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.19</td>
    <td align="right">55.60</td>
    <td align="right">40.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.60</td>
    <td align="right">26.12</td>
    <td align="right">26.31</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.70</td>
    <td align="right">29.10</td>
    <td align="right">29.07</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.88</td>
    <td align="right">31.10</td>
    <td align="right">30.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.97</td>
    <td align="right">46.34</td>
    <td align="right">35.10</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.57</td>
    <td align="right">39.79</td>
    <td align="right">27.58</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.01</td>
    <td align="right">51.78</td>
    <td align="right">40.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.64</td>
    <td align="right">54.42</td>
    <td align="right">38.56</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.08</td>
    <td align="right">52.87</td>
    <td align="right">35.13</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.18</td>
    <td align="right">61.24</td>
    <td align="right">43.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.73</td>
    <td align="right">55.38</td>
    <td align="right">39.34</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.72</td>
    <td align="right">64.66</td>
    <td align="right">44.60</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.68</td>
    <td align="right">64.08</td>
    <td align="right">44.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.10</td>
    <td align="right">42.93</td>
    <td align="right">34.99</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.52</td>
    <td align="right">53.29</td>
    <td align="right">40.36</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">36.69</td>
    <td align="right">59.93</td>
    <td align="right">60.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.30</td>
    <td align="right">60.38</td>
    <td align="right">35.34</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.17</td>
    <td align="right">60.97</td>
    <td align="right">38.08</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.63</td>
    <td align="right">77.46</td>
    <td align="right">77.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.75</td>
    <td align="right">74.12</td>
    <td align="right">35.88</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.89</td>
    <td align="right">80.24</td>
    <td align="right">39.85</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.38</td>
    <td align="right">83.66</td>
    <td align="right">83.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">52.49</td>
    <td align="right">93.68</td>
    <td align="right">37.31</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.44</td>
    <td align="right">94.32</td>
    <td align="right">39.24</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.15</td>
    <td align="right">118.65</td>
    <td align="right">118.86</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.14</td>
    <td align="right">35.42</td>
    <td align="right">11.27</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">66.75</td>
    <td align="right">59.66</td>
    <td align="right">46.03</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">22.90</td>
    <td align="right">20.76</td>
    <td align="right">25.54</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.39</td>
    <td align="right">22.07</td>
    <td align="right">26.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">96.88</td>
    <td align="right">85.18</td>
    <td align="right">47.28</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.03</td>
    <td align="right">21.89</td>
    <td align="right">24.81</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">28.03</td>
    <td align="right">23.18</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">121.07</td>
    <td align="right">107.42</td>
    <td align="right">47.41</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">27.27</td>
    <td align="right">23.82</td>
    <td align="right">25.94</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">32.14</td>
    <td align="right">26.07</td>
    <td align="right">28.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">174.19</td>
    <td align="right">149.71</td>
    <td align="right">50.78</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">33.57</td>
    <td align="right">29.30</td>
    <td align="right">30.20</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">37.73</td>
    <td align="right">29.52</td>
    <td align="right">30.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.00</td>
    <td align="right">42.44</td>
    <td align="right">41.98</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.70</td>
    <td align="right">42.28</td>
    <td align="right">41.89</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.96</td>
    <td align="right">30.05</td>
    <td align="right">30.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">29.72</td>
    <td align="right">56.93</td>
    <td align="right">57.54</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.51</td>
    <td align="right">58.73</td>
    <td align="right">59.01</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.78</td>
    <td align="right">39.76</td>
    <td align="right">29.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.77</td>
    <td align="right">78.22</td>
    <td align="right">78.30</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">49.09</td>
    <td align="right">80.55</td>
    <td align="right">80.17</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">31.90</td>
    <td align="right">61.36</td>
    <td align="right">45.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">49.07</td>
    <td align="right">90.06</td>
    <td align="right">90.40</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">57.82</td>
    <td align="right">97.54</td>
    <td align="right">96.24</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">37.21</td>
    <td align="right">68.67</td>
    <td align="right">50.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.90</td>
    <td align="right">30.95</td>
    <td align="right">31.02</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.63</td>
    <td align="right">33.47</td>
    <td align="right">33.51</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.76</td>
    <td align="right">35.59</td>
    <td align="right">35.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">19.91</td>
    <td align="right">50.31</td>
    <td align="right">39.30</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.44</td>
    <td align="right">42.29</td>
    <td align="right">30.13</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">21.84</td>
    <td align="right">56.24</td>
    <td align="right">44.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">32.47</td>
    <td align="right">80.20</td>
    <td align="right">46.43</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">35.13</td>
    <td align="right">57.44</td>
    <td align="right">39.26</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">33.86</td>
    <td align="right">66.11</td>
    <td align="right">48.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">37.15</td>
    <td align="right">68.72</td>
    <td align="right">52.33</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">36.87</td>
    <td align="right">71.95</td>
    <td align="right">50.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">38.20</td>
    <td align="right">74.03</td>
    <td align="right">52.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.43</td>
    <td align="right">43.47</td>
    <td align="right">38.28</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.41</td>
    <td align="right">54.76</td>
    <td align="right">43.82</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.52</td>
    <td align="right">60.83</td>
    <td align="right">61.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">38.54</td>
    <td align="right">61.18</td>
    <td align="right">37.71</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">45.59</td>
    <td align="right">63.26</td>
    <td align="right">40.52</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">48.40</td>
    <td align="right">78.23</td>
    <td align="right">77.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">44.87</td>
    <td align="right">75.97</td>
    <td align="right">38.53</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">55.20</td>
    <td align="right">84.70</td>
    <td align="right">43.19</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">51.80</td>
    <td align="right">84.65</td>
    <td align="right">84.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">60.04</td>
    <td align="right">104.25</td>
    <td align="right">43.83</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">72.18</td>
    <td align="right">107.53</td>
    <td align="right">46.52</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">73.46</td>
    <td align="right">124.27</td>
    <td align="right">125.96</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
